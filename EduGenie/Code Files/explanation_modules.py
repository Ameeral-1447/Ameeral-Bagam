import os, time
from dotenv import load_dotenv
load_dotenv()
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Fallback list - onnu overload aana aduthathu try pannum
MODELS = ["gemini-3.6-flash", "gemini-3.5-flash", "gemini-3.5-flash-lite", "gemini-2.0-flash"]

def call_gemini(prompt):
    for model_name in MODELS:
        try:
            print(f"Trying {model_name}...")
            res = client.models.generate_content(model=model_name, contents=prompt)
            return res.text
        except Exception as e:
            print(f"{model_name} failed: {e}")
            time.sleep(1)
            continue
    return "Error: All models are busy da, 30 sec kalichu try pannu da!"

def explain_topic(topic, level="beginner"):
    prompt = f"Explain {topic} for {level} level in simple way with examples"
    return call_gemini(prompt)