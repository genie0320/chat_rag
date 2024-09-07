import os
import sys
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs4
from io import StringIO


def convert_updown(updown_value):
    """
    '전일비' : '하락    500' >> -500 으로 변경해줌.
    """
    updown_value = updown_value.replace(",", "")  # 숫자에 있는 콤마 제거
    if "상승" in updown_value:
        return int(updown_value.split()[1])
    elif "하락" in updown_value:
        return -int(updown_value.split()[1])
    elif "보합" in updown_value:
        return 0
    return updown_value


url = "https://finance.naver.com/sise/sise_market_sum.naver"

# 세션생성
session = requests.Session()
res = session.get(url)
# session.cookies.get_dict()

# 사용자에게 보여줄 선택지를 추출하는 과정.
res_html = bs4(res.text, "html.parser")

check_box_html = res_html.find_all("input", type="checkbox")
check_boxes = {}

for x in check_box_html:
    vars = x.get("value")
    vals = x.find_next_sibling("label").text
    check_boxes[vals] = vars

# 사용자선택과 query_string 생성.
_user_input = input(f"Select item : {check_boxes.keys()}")

user_input = list(map(str, _user_input.split(",")))
query_string = "&".join(
    [f"fieldIds={check_boxes[value.strip()]}" for value in user_input]
)


# [중요] 일단 쿼리URL을 날려서 값을 세팅해둔다. (서버쪽 세션에 저장되는 듯)
url2 = f"https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http://finance.naver.com/sise/sise_market_sum.naver?&{query_string}"
res1 = session.get(url2)


# [중요] 이제는 앞에 복잡한 설정 없이, 단순히 페이지수만 바꿔가며 날리면 된다.
for page in range(1, 3):
    url4 = f"https://finance.naver.com/sise/sise_market_sum.naver?&page={page}"

    res1 = session.get(url4)
    html_content = StringIO(res1.text)  # 새로 바뀐 부분.
    df_list = pd.read_html(html_content)
    df = df_list[1]

    # clean up data
    df.dropna(axis="index", how="all", inplace=True)
    df.dropna(axis="columns", how="all", inplace=True)

    if df.empty:
        print("DataFrame is empty.")
        sys.exit()
    else:
        if "전일비" in df.columns:
            df["전일비"] = df["전일비"].apply(convert_updown)

        # 4. 데이터 저장
        if os.path.exists("output.csv"):
            df.to_csv(
                "output.csv", encoding="utf-8-sig", index=False, header=0, mode="a"
            )
        else:
            df.to_csv("output.csv", encoding="utf-8-sig", index=False)
        print(f"{page} 스크랩완료")

print("스크랩완료")
