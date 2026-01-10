FROM python:3.11-slim

WORKDIR /app

# Install only what's needed for the Gemini SDK
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Use environment variables for the API Key
ENV GOOGLE_API_KEY="your-key-here"

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
