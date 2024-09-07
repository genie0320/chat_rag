# 데이터수집 with python

## 개요
## 도구들

### python library & package
데이터수집에 이용할 수 있는 도구들은 꽤 많다. 하지만 문서화가 다 잘 되어 있는 것은 아니다. 이를테면...셀레니움같은 경우 이제껏 보면서 가장 문서화가 안 되어 있다(심지어 개인 API 관리자보다도 못하다).

하지만 나머지는 꽤 문서화가 잘 되어 있어서 파면 팔수록 새로운 것이 발견되는 즐거움을 준다. 아래는 알려진 도구들과 그 공식문서로 바로가는 링크.  
- [requests](https://requests.readthedocs.io/en/latest/) + [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) : python으로 데이터수집을 시작할 때 가장 처음으로 사용하게 될 가벼운 도구들. 익히는 방법도 어렵지 않고, 그렇게 익혀둔 '개념'들은 아래의 다른 툴들을 다룰 때 도움이 된다. 
- [selenium](https://www.selenium.dev/) : 화면을 불러와서 로그인처리를 하는 등, 웹과 인터렉션을 할 수 있다는 점에서는 독보적이다. 하지만 위에서도 말한 것처럼 문서화가 정말... %#@%&^@%$ 
- [scrapy](https://scrapy.org/) : 위의 2가지가 엄밀히 '웹스크랩'에 이용되는 도구라면, 웹세상 오만군데를 떠돌아다니며 자기 혼자 링크를 찾고 방문을 해서 나름의 색인을 만들어야 하는 '웹크롤링'을 위한 도구이다.
- urllib3 : 사실 다른 툴로 스크래핑을 할 때, url을 조작하는 용도로 쭈욱 사용해왔다. 하지만 이걸로도 requests와 비슷한 역할을 할 수 있다는 걸 엊그제 처음 알았다. 문서에 따르자면 심지어 꽤나 강력하다. 

- Playwright : 마소에서 만든 웹자동화 툴이다. 브라우저계에서 영원히 고통받고 있는 그들의 입장을 대변이라도 하듯, 광범위한 브라우저에서 다양한 언어로 사용할 수 있다는 것이 장점이다. 
- Puppeteer : 구글에서 웹테스팅 툴이다. 당연히 크롬계열의 브라우저에서 가장 성능이 좋고, 아쉽게도 javascript만 지원한다. 파이어폭스지원이 좀 불안하다는 단점이 있기는 하지만, 만약 크롬+js환경 개발자라면 가장 '쉽고 가벼운' 선택이 될 듯.
- [trafilatura](https://trafilatura.readthedocs.io/en/latest/index.html) : 최근에 발견했는데, 그다지 복잡하지 않은 구성을 가진 화면이라면, 불러오는 것만으로도 요소선택없이 나름대로 데이터를 잘 저장해주며, xml이나 json등으로 결과물을 뽑는것도 가능하다. 당연히 site RAG를 만들때 오만 쓸데없는 정보없이 필요한 정보만 쉽게 뽑아낼 수 있어서 매우 유용할 듯 하다. 
    - [예시영상(영어)](https://www.youtube.com/watch?v=6K1lyyzpxtk) 
    - [유튜브 플레이리스트 (프로그래머 김플스튜디오)](https://www.youtube.com/watch?v=945F3SxW7Tk&list=PL5bK87xH5V1xkEvVYBupHYNUtIEAiLIzL)

### 유료 스크래핑&프록시관리 API들
- ZenRows : 유료 스크래핑 API다. 얼마나 강력한진 몰라도 유료(유로화결제)다. 심지어 프리티어도 없다. 
- [기타](https://medium.com/@spaw.co/zenrows-alternative-11ab3af27903) 

### API들

