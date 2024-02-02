# !pip install langchain langchain-openai streamlit beautifulsoup4 chroma
# !pip install Jupytext # Need only in jupyter env. then run 'jupytext --to py app.ipynb'

from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings

load_dotenv()


def get_response(user_input):
    return "Loading..."


def get_vectorstore_from_url(url):
    # get the text in the website
    loader = WebBaseLoader(url)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(documents)

    vector_store = Chroma.from_documents(document_chunks, OpenAIEmbeddings())
    return vector_store


# App config
st.set_page_config(page_title="Chat with websites", page_icon="🤖")
st.title("Chat with website")


# chat_history가 variable이 아니라 str로 들어간다는 것에 주의.
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="{$site.title} 입니다. 무엇이 궁금하신가요?"),
    ]

# Sidebar
with st.sidebar:
    st.header("settings")
    website_url = st.text_input("Input website URL")

"""
https://python.langchain.com/docs/get_started/introduction
"""

if website_url is None or website_url == "":
    st.info("웹사이트 주소를 입력해주세요.")
else:
    document_chunks = get_vectorstore_from_url(website_url)

    # For debug
    # with st.sidebar:
    #     st.write(document_chunks)

    # initial setting
    user_input = st.chat_input("무엇이 궁금하신가요?")

    # chat ui
    if user_input is not None and user_input != "":
        response = get_response(user_input)
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        st.session_state.chat_history.append(AIMessage(content=response))

    # For debug
    # with st.sidebar:
    #     st.write(st.session_state.chat_history)

    # conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("human"):
                st.write(message.content)
