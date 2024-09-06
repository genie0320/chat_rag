# Session 과 Cookies 에 대해서.

멀쩡한 requests를 놔두고 Session을 공부하게 된 것은 순수히 착각에 의한 것이었다. 아는 게 병이라고 네이버 금융페이지에서 항목설정을 바꿔 로딩을 하고 싶었는데, 매번 네이버금융의 기본설정대로만 데이터를 읽어오는 것이었다. 

내 생각엔... 내 컴퓨터의 정보를 쿠키 또는 세션에 저장하고, 마지막에 실행되었던 결과를 그대로 보여주는 것 같았다. 다시 생각해보면 우스운 일인데... 여러가지를 실험해봐도 도무지 뾰족한 수가 나지 않아서 세션을 공부하게 되었다...(하지만 실험 도중에 내가 url 생성을 잘못된 방법으로 하고 있었다는 걸 깨달았다. 그냥 심플한 requests.get 만으로도 충분히 스크래핑은 가능했다.)

어제오늘 이틀동안 머리 싸매며 공부했던게 너무 억울해서 기록을 남겨 놓기로 한다.

## Session 이란.
나는 어렴풋하게만 알고 있었는데, 쿠키와 세션은 다음과 같은 차이가 있었다. 
- 세션정보 : 클라이언트-서버 양쪽 모두에 저장되는 정보
- 쿠키정보 : 클라이언트에만 저장되는 정보

나중에라도 서버정보와 맞춰볼 수 있는 세션정보와는 달리 클라이언트에만 저장되며 심지어 매우 손쉽게 수정이 가능한 쿠키정보는, '봐도 상관없을 정도록 망가뜨려진' 정보의 형태로 저장되며, 각 사이트마다 다르게 관리된다. 
> 쿠키정보는 개발자모드 진입 후 `Application`탭의 Storage > Coolies > 각 도메인에서 손쉽게 확인할 수 있다.

## Session 과 requests 의 차이

GPT에 따르자면, requests가 매번 호출될 때마다 새로운 connection을 만드는 것에 반해, session은 최초 연결시의 headers, cookies 등의 정보가 포함된 connection 객체를 생성하여 쭈욱 활용한다. 따라서 비용적으로나 성능적으로나 효율적이다. 

```python
import requests

url = 'http://***'

# session 객체를 생성한다. 
session = requests.Session()

# session 객체에 다양한 변형을 가할 수 있다. 특히 user_agent 정보. 
session.headers["User-Agent"] = user_agent
session.params = params

# session으로 response 받아오기.
session.get(url)

# 쿠키정보를 확인할 수 있다. 
session.cookies.get_dict()
```