import os, time
from dotenv import load_dotenv
load_dotenv()
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODELS = ["gemini-3.6-flash", "gemini-3.5-flash", "gemini-3.5-flash-lite", "gemini-2.0-flash"]

def call_gemini(prompt):
    for m in MODELS:
        try:
            print(f"Trying {m} for Quiz...")
            res = client.models.generate_content(model=m, contents=prompt)
            return res.text
        except:
            time.sleep(1)
            continue
    return "Error: All models busy da!"

def generate_quiz(topic, num=5):
    prompt = f"Generate {num} MCQs on {topic} with 4 options each and correct answer at end. Make it fun."
    return call_gemini(prompt)