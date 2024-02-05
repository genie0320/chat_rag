from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI


# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
tinyllama_llm = ChatOpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

tinyllama_llm.invoke("My name is genie, how are you?")
# memory = ConversationBufferMemory()

# conversation = ConversationChain(llm=tinyllama_llm, vervose=True, memory=memory)

# conversation.predict(input="Hi. my name is genie")
