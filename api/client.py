# client.py

import requests
import streamlit as st

def get_openai_response(input_text):
    # Use requests.get and pass the topic as a parameter
    response = requests.get("http://localhost:8001/es say",
                            params={'topic': input_text})
    
    # Access the correct key: 'response'
    return response.json()['response']

def get_ollama_response(input_text):
    # Use requests.get and pass the topic as a parameter
    response = requests.get("http://localhost:8001/poem",
                            params={'topic': input_text})
    
    # Access the correct key: 'response'
    return response.json()['response']


## Streamlit framework
st.title("Langchain Demo with GEMMA3 API")
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1)) # Corrected to use input_text1