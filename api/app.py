from fastapi import FastAPI, Query
from langchain_cohere import ChatCohere
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

os.environ['COHERE_API_KEY'] = os.getenv("COHERE_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version="1.0", 
    description="API Server with Cohere and Ollama"
)

# Initialize the language models
cohere_model = ChatCohere(model="command", temperature=0.7)
ollama_model = OllamaLLM(model="gemma3:1b")


@app.get("/essay")
def generate_essay_get(topic: str):
    """Generates an essay using the Cohere model."""

    question = f"Write me an essay about {topic} with 100 words"
    # ChatCohere returns an AIMessage object, so we access content
    response_object = cohere_model.invoke(question)
    return {"response": response_object.content}


@app.get("/poem")
def generate_poem_get(topic: str):
    """Generates a poem using the local Ollama model."""

    question = f"Write me a poem about {topic} for a 5 year old child with 100 words"
    # OllamaLLM returns a simple string
    response_string = ollama_model.invoke(question)
    return {"response": response_string}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
