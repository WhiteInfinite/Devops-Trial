import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

app = FastAPI()
client = genai.Client(api_key=os.environ.get("AIzaSyCCjtzA50EJqB5TDrGUJ57MCwdm4g13c9I"))

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
