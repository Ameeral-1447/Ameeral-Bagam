import os, time
from dotenv import load_dotenv
load_dotenv()
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODELS = ["gemini-3.6-flash", "gemini-3.5-flash", "gemini-3.5-flash-lite", "gemini-2.0-flash"]

def call_gemini(prompt):
    for m in MODELS:
        try:
            res = client.models.generate_content(model=m, contents=prompt)
            return res.text
        except:
            time.sleep(1)
            continue
    return "Error: All models busy da!"

def summarize_text(text):
    prompt = f"Summarize this text in 5 bullet points in simple language: {text}"
    return call_gemini(prompt)