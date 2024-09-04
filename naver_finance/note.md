# Scrap naver finance

## urlparse
```python
from urllib.parse import urlparse, urlunparse

parsed_url = urlparse(base_url)
    # ParseResult(
    #   scheme='https', 
    #   netloc='finance.naver.com', 
    #   path='/sise/field_submit.naver', 
    #   params='', 
    #   query='', 
    #   fragment='')

combined_url = urlunparse(
    (
        parsed_url.scheme,  
        parsed_url.netloc,  
        parsed_url.path,  
        # url뒤에 붙을 때 각 기호(; &, #)가 프리픽스로 붙는다.
        "", # parsed_url.params
        f"{query_string}&{user_query}&page={page}", # query
        "", # parsed_url.fragment
    )
)
```

## 판다스의 놀라운 기능. 
html에서 table을 뽑아와서 df로 만들어준다!!

```python
# encoding을 지정해줘야 한글이 안 깨진다.
df = pd.read_html(combined_url, header=0, encoding="cp949")

# 여러개의 table이 있는 경우에는 다음과 같이 순서를 지정.
df = pd.read_html(combined_url, header=0, encoding="cp949")[1]
```