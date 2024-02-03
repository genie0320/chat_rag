# Chat with website
> tag : RAG, openai, langchain, chromadb, beautifulsoup4, streamlit

사용자 지정웹사이트의 내용을 기반으로 AI와 채팅할 수 있는 서비스. 이 기능을 통해 원하는 맥락이 반영된 답변을 얻을 수 있다. 

## User story

1. 사용자는 URL을 입력한다.
2. 서비스는 해당 URL의 정보에 대해서 공부한다.
3. 사용자의가 질문을 입력한다.
4. 서비스는 공부했던 내용 중에서 질문과 관련이 있는 부분을 찾아 llm에게 넘기고, 답변을 생성한다. 

## Change log
v0.1 기본적인 RAG기능 구현 완료