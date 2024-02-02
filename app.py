# !pip install langchain langchain-openai streamlit
# !pip install Jupytext # Need only in jupyter env. then run 'jupytext --to py app.ipynb'

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage


def get_response(user_input):
    return "Loading..."


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
    website_url = st.text_input("website URL")

if website_url is None or website_url == "":
    st.info("웹사이트 주소를 입력해주세요.")
else:
    # initial setting
    user_input = st.chat_input("무엇이 궁금하신가요?")

    # chat ui
    if user_input is not None and user_input != "":
        response = get_response(user_input)
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        st.session_state.chat_history.append(AIMessage(content=response))

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
