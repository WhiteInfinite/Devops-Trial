import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

app = FastAPI(title="Gemini 2.0 Flash Proxy")

# Initialize Gemini Client
# The SDK automatically looks for the GEMINI_API_KEY environment variable
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

class Query(BaseModel):
    text: str

@app.post("/generate")
async def generate_text(query: Query):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=query.text
        )
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "healthy"}
