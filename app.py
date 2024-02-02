# !pip install langchain langchain-openai streamlit
# !pip install Jupytext # Need only in jupyter env. then run 'jupytext --to py app.ipynb'

import streamlit as st


def get_response(user_input):
    return "Loading..."


# App config
st.set_page_config(page_title="Chat with websites", page_icon="🤖")
st.title("Chat with website")

# Sidebar
with st.sidebar:
    st.header("settings")
    website_url = st.text_input("website URL")

# initial setting
user_input = st.chat_input("무엇이 궁금하신가요?")
with st.chat_message("AI"):
    st.write("What can I help you?")

# chat ui
if user_input is not None and user_input != "":
    response = get_response(user_input)
    with st.chat_message("human"):
        st.write(user_input)
    with st.chat_message("AI"):
        st.write(response)
