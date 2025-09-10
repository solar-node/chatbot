from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_cohere import ChatCohere
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms.ollama import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['COHERE_API_KEY']=os.getenv("COHERE_API_KEY") 

app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description = "A simple API server"
)

add_routes(
    app,
    ChatCohere(model="command-nightly", temperature=0.7),
    path = "/ChatCohere"
)

model = ChatCohere(model="command-nightly", temperature=0.7)

## Ollama LLAMA2
llm = Ollama(model="gemma3:1b")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words ")
prompt2=ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words ") 

add_routes(
    app,
    prompt1|model,
    path="/essay"
    
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__ == "__main__" : 
    uvicorn.run(app, host="localhost", port=8000)
