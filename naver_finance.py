import os
import sys
import json
import requests

import pandas as pd
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlparse, urlunparse


url = "https://finance.naver.com/sise/sise_market_sum.naver"

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
page = 1

parsed_url = urlparse(base_url)

query_string = "&".join([f"{key}={value}" for key, value in payload.items()])

for i in range(1, 100):
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

    # 3. 불러온 html에서 table만을 추출하여 가공.
    df = pd.read_html(combined_url, header=0, encoding="cp949")[1]

    if df is not None:
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
