from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv() 

os.environ["COHERE_API_KEY"] = os.getenv("COHERE_API_KEY")

## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

## Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to user quaries"),
        ("user", "Question:{question}")

    ]
)

## Streamlit framework
st.title('Langchain demo with Cohere AI')
input_text = st.text_input("Search the topic you want")

## OpenAI LLM
llm = ChatCohere(model="command-nightly", temperature=0.7)
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))

print("Langchain API Key:", os.getenv("LANGCHAIN_API_KEY"))
print("Cohere API Key:", os.getenv("COHERE_API_KEY"))
