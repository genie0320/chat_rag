# 애증의 pandas

## read_html
html에서 table을 뽑아와서 df로 만들어준다!!
이번에 새로 변경된 부분이 있어 추가해둔다.
*이전처럼 사용할 수도 있지만 계속 warning이 뜬다.*
신기하게도 별 인코딩을 하지 않아도 잘만 불러온다.
```python
from io import StringIO

res1 = session.get(url4)
html_content = StringIO(res1.text)  # 새로 바뀐 부분.
df_list = pd.read_html(html_content)

# 옛날방식
# encoding을 지정해줘야 한글이 안 깨진다.
# df = pd.read_html(combined_url, header=0, encoding="cp949")

# 여러개의 table이 있는 경우에는 다음과 같이 순서를 지정.
# df = pd.read_html(combined_url, header=0, encoding="cp949")[1]
```

## tips
```python
# clean up data
df.dropna(axis="index", how="all", inplace=True)
df.dropna(axis="columns", how="all", inplace=True)

# 해당 df가 비어 있는지 확인하는 방법
df.empty # True / False
```