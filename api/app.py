from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
import os

load_dotenv() 

app = FastAPI(
    title="Langchain Server",
    version="1.0", 
    description="API Server"
)

# Initialize models with API key
openai_model = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
ollama_model = OllamaLLM(model="gemma3:1b")

# Pydantic request models
class EssayRequest(BaseModel):
    topic: str

class PoemRequest(BaseModel):
    topic: str

# POST endpoint for essay (OpenAI)
@app.post("/essay")
def generate_essay(request: EssayRequest):
    question = f"Write me an essay about {request.topic} with 100 words"
    response = openai_model.invoke({"question": question})
    return {"response": response.get("text", str(response))}

# POST endpoint for poem (Ollama)
@app.post("/poem")
def generate_poem(request: PoemRequest):
    question = f"Write me a poem about {request.topic} for a 5 years child with 100 words"
    response = ollama_model.invoke({"question": question})
    return {"response": response.get("text", str(response))}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)