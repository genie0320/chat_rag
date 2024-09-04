# Standard library imports
import os
import sys
import json
import requests

# Third party imports
import pandas as pd
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlparse, urlunparse

# Local application imports

# 1. 쿼리 항목 선택
url = "https://finance.naver.com/sise/sise_market_sum.naver"
# https://finance.naver.com/sise/sise_market_sum.naver?&page=2

res = requests.get(url)
soup = bs4(res.text, "html.parser")

# User selection item
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

for i in user_input:
    val = user_example[i]
    user_selections.append(check_boxes[val])

# -------------------------------
# 원래는 아래서 urlparse로 해결하고 싶었지만,
# 이놈들이 'fieldIds'라는 동일한 키를 반복해서 사용하는 바람에
# 여러개의 쿼리를 붙이기 위해선 우회할 수 밖에 없었다.
# -------------------------------
# fieldIds=quant&fieldIds=ask_buy&fieldIds=amount
user_query = "&".join([f"fieldIds={value}" for value in user_selections])


# 2. 사용자 선택을 기준으로 다음 URL 재구성.
base_url = "https://finance.naver.com/sise/sise_market_sum.naver"
payload = {
    "menu": "market_sum",
    "returnUrl": "http://finance.naver.com/sise/sise_market_sum.naver",
}
page = 1

parsed_url = urlparse(base_url)
# ParseResult(scheme='https', netloc='finance.naver.com', path='/sise/field_submit.naver', params='', query='', fragment='')

query_string = "&".join([f"{key}={value}" for key, value in payload.items()])

for i in range(1, 100):
    # urlunparse 에는 7개의 인자를 넣어줘야 하며, 각 인자마다 prefix가 달라진다.
    combined_url = urlunparse(
        (
            parsed_url.scheme,  # scheme='https'
            parsed_url.netloc,  # netloc='finance.naver.com'
            parsed_url.path,  # path='/sise/field_submit.naver'
            "",  # ;
            f"{query_string}&{user_query}&page={page}",  # &
            "",  # #
        )
    )

    # 3. 불러온 html에서 table만을 추출하여 가공.
    # 모든 테이블을 불러오므로... 몇번째 table인지를 찍어줘야 한다.
    df = pd.read_html(combined_url, header=0, encoding="cp949")[1]

    if df is not None:

        # 필요없는 라인을 삭제.
        df.dropna(axis="index", how="all", inplace=True)
        df.dropna(axis="columns", how="all", inplace=True)

        # 4. 데이터 저장
        if os.path.exists("output.csv"):
            df.to_csv(
                "output.csv", encoding="utf-8-sig", index=False, header=0, mode="a"
            )
        else:
            df.to_csv("output.csv", encoding="utf-8-sig", index=False)

        page += 1
    else:
        sys.exit()
