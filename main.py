import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

app = FastAPI()
client = genai.Client(api_key=os.environ.get("##############################"))

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

# Install 'tenacity' first: pip install tenacity
from tenacity import retry, wait_random_exponential, stop_after_attempt

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(5))
def get_gemini_response(text):
    return client.models.generate_content(model="gemini-2.0-flash", contents=text)
