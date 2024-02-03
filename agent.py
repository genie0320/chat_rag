from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from bs4 import BeautifulSoup as bs4
import requests

load_dotenv()

MODEL = "gpt-3.5-turbo-0125"
template = """Answer to the following question based on the context:

Question : {question}

Context :

{context}"""

prompt = ChatPromptTemplate.from_template(template)


def scrape_txt(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = bs4(response.text, "html.parser")

            page_txt = soup.get_text(separator=" ", strip=True)

            return page_txt
        else:
            return f"Something wrong : Status code {response.status_code}"
    except Exception as e:
        print(e)
        return f"Failed to load : {e}"


url = "https://blog.langchain.dev/announcing-langsmith/"

page_content = scrape_txt(url)[:1000]

chain = prompt | ChatOpenAI(model=MODEL) | StrOutputParser()

chain.invoke({"question": "What is langsmith?", "context": page_content})
