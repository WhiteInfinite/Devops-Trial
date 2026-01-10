import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

app = FastAPI()
client = genai.Client(api_key=os.environ.get("AIzaSyD5doCWlOl-1lB8GkT0v6bUxnM5H0IITAA"))

class Query(BaseModel):
    text: str

@app.post("/generate")
async def generate(query: Query):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=query.text
        )
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health(): return {"status": "ok"}
