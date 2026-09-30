import os, time
from dotenv import load_dotenv
load_dotenv()
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODELS = ["gemini-3.6-flash", "gemini-3.5-flash", "gemini-3.5-flash-lite", "gemini-2.0-flash"]

def call_gemini(prompt):
    for m in MODELS:
        try:
            print(f"Trying {m} for Q&A...")
            res = client.models.generate_content(model=m, contents=prompt)
            return res.text
        except Exception as e:
            print(f"{m} fail: {e}")
            time.sleep(1)
            continue
    return "Error: All models busy da, 30 sec wait panni try pannu!"

def answer_question(question):
    prompt = f"Answer this question in simple way: {question}"
    return call_gemini(prompt)