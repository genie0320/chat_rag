# Scrap naver finance

## urlparse
쓸 일이 있겠나 싶지만, url을 안전하게 unicode로 변환해준다.
네이버의 경우, unicode로 변환하면 제대로 된 정보를 주지만, 디코드된 url을 던졌을 때는 그렇지 않았다. 하지만 다시 사용할 수 있을 것 같지 않아, 세션을 이용하는 다른 방법으로 우회해서 진행했다.
```python
from urllib.parse import urlparse, urlunparse

base_url = "https://finance.naver.com/sise/sise_market_sum.naver"
page = 1

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

