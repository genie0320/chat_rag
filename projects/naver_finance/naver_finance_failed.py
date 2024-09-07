# ----------------------------------
# 아래 코드는...세션을 활용하지 않아 실패한 것으로.
# ----------------------------------

import os
import sys
from urllib.parse import urlparse, urlunparse
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs4


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
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
res = requests.get(url)
soup = bs4(res.text, "html.parser")

check_box_html = soup.find_all("input", type="checkbox")
check_boxes = {}

for x in check_box_html:
    vars = x.get("value")
    vals = x.find_next_sibling("label").text
    check_boxes[vals] = vars

# 사용자가 숫자만 선택하면 되도록 key()를 뽑아 번호를 지정하여 노출.
_user_example = check_boxes.keys()
user_example = dict(enumerate(_user_example))

# 사용자가 입력받기 & 여러개 선택시 숫자를 추출하여 원본과 대조하여 query_param을 만든다.
_user_input = input(f"Select item no : {user_example}")

user_input = list(map(int, _user_input.split(",")))
user_selections = []

print(user_selections)

for i in user_input:
    val = user_example[i]
    user_selections.append(check_boxes[val])

user_query = "&".join([f"fieldIds={value}" for value in user_selections])

# 2. 사용자 선택을 기준으로 다음 URL 재구성.
base_url = "https://finance.naver.com/sise/sise_market_sum.naver"
payload = {
    "menu": "market_sum",
    "returnUrl": "http://finance.naver.com/sise/sise_market_sum.naver",
}

parsed_url = urlparse(base_url)

query_string = "&".join([f"{key}={value}" for key, value in payload.items()])

for page in range(1, 3):
    combined_url = urlunparse(
        (
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            "",
            f"{query_string}&{user_query}&page={page}",
            "",
        )
    )
    print(combined_url)
    print("-----------------------------------------------")

    # 3. 불러온 html에서 table만을 추출하여 가공.
    df = pd.read_html(combined_url, header=0, encoding="cp949")[1]

    print(df)
    if df is not None:

        # clean up data
        df.dropna(axis="index", how="all", inplace=True)
        df.dropna(axis="columns", how="all", inplace=True)

        if df["전일비"].any():
            df["전일비"] = df["전일비"].apply(convert_updown)

        # 4. 데이터 저장
        if os.path.exists("output.csv"):
            df.to_csv(
                "output.csv", encoding="utf-8-sig", index=False, header=0, mode="a"
            )
        else:
            df.to_csv("output.csv", encoding="utf-8-sig", index=False)
        print(f"{page} 스크랩완료")

    else:
        sys.exit()

print("스크랩완료")
