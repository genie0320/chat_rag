# !pip install langchain langchain-openai streamlit beautifulsoup4 chroma python-dotenv
# !pip install Jupytext # Need only in jupyter env. then run 'jupytext --to py app.ipynb'

from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

load_dotenv()


def get_response(user_input):
    return "Loading..."


def get_vectorstore_from_url(url):
    # get the text in the website

    if "embedding_count" not in st.session_state:
        st.session_state.embedding_count = [
            "embedding",
        ]
    else:
        st.session_state.embedding_count.append("embedding...")
        with st.sidebar:
            for count in st.session_state.embedding_count:
                st.write(count)

    loader = WebBaseLoader(url)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(documents)

    db = Chroma.from_documents(document_chunks, OpenAIEmbeddings())
    return db


def get_context_retriever_chain(vector_store):
    llm = ChatOpenAI()
    retriever = vector_store.as_retriever()

    prompt = ChatPromptTemplate.from_messages(
        [
            MessagesPlaceholder(variable_name="chat_history"),
            (
                "system",
                "According to below conversation, generate a search query to look up in order to get information relevant to the conversation.",
            ),
            ("user", "{input}"),
        ]
    )

    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

    return retriever_chain


def get_conversational_rag_chain(retriever_chain):
    llm = ChatOpenAI()
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Answer the user's questions based on the below context:\n\n{context}",
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
        ]
    )
    stuff_documents_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever_chain, stuff_documents_chain)


# App config
st.set_page_config(page_title="Chat with websites", page_icon="🤖")
st.title("Chat with website")


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
    # chat_history가 variable이 아니라 str로 들어간다는 것에 주의.
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            # AIMessage(content="{$site.title} 입니다. 무엇이 궁금하신가요?"),
            AIMessage(content="How can I help you?"),
        ]
    if "db" not in st.session_state:
        # Create conversational chain
        st.session_state.db = get_vectorstore_from_url(website_url)

    # For debug
    # with st.sidebar:
    #     st.write(document_chunks)

    # initial setting
    retriever_chain = get_context_retriever_chain(st.session_state.db)

    conversation_rag_chain = get_conversational_rag_chain(retriever_chain)

    # chat ui
    user_input = st.chat_input("무엇이 궁금하신가요?")
    if user_input is not None and user_input != "":
        # response = get_response(user_input)
        # st.session_state.chat_history.append(HumanMessage(content=user_input))
        # st.session_state.chat_history.append(AIMessage(content=response))
        response = conversation_rag_chain.invoke(
            {"chat_history": st.session_state.chat_history, "input": user_input}
        )

        retrieved_documents = retriever_chain.invoke(
            {"chat_history": st.session_state.chat_history, "input": user_input}
        )
        st.write(retrieved_documents)
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
