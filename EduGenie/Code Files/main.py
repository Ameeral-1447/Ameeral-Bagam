from flask import Flask, request, jsonify, render_template
from google import genai

app = Flask(__name__)
client = genai.Client(api_key="AQ.Ab8RN6KQyvM7ic8OGZ2mlbF31kQ3gyLUNZH39X5al5S_cbsCJA")
# ==============================

# Gemini call panna oru common function
def ask_gemini(prompt):
    models_to_try = [
        "gemini-3.5-flash-lite",
        "gemini-3.5-flash",
        "gemini-2.5-flash-lite"
    ]
    last_error = ""
    for model_name in models_to_try:
        try:
            print(f"Trying model: {model_name}")
            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            if response and response.text:
                return response.text
        except Exception as e:
            last_error = str(e)
            print(f"{model_name} failed: {e}")
            continue
    
    return f"Google server busy da, 30 sec kalichu try pannu! Error: {last_error}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/explain', methods=['POST'])
def explain():
    data = request.get_json()
    question = data.get('question', '')
    prompt = f"Explain '{question}' in a very simple, beginner-friendly way with Tamil + English examples."
    answer = ask_gemini(prompt)
    return jsonify({"answer": answer})

@app.route('/qna', methods=['POST'])
def qna():
    data = request.get_json()
    question = data.get('question', '')
    prompt = f"Answer this question clearly: {question}"
    answer = ask_gemini(prompt)
    return jsonify({"answer": answer})

@app.route('/quiz', methods=['POST'])
def quiz():
    data = request.get_json()
    topic = data.get('topic', '')
    prompt = f"Create 5 MCQs with answers for the topic: {topic}. Format as Q1, Options A,B,C,D, and correct answer."
    answer = ask_gemini(prompt)
    return jsonify({"answer": answer})

@app.route('/learning_path', methods=['POST'])
def learning_path():
    data = request.get_json()
    topic = data.get('topic', '')
    prompt = f"Create a step-by-step learning roadmap for a beginner to learn {topic}"
    answer = ask_gemini(prompt)
    return jsonify({"answer": answer})

@app.route('/summary', methods=['POST'])
def summary():
    data = request.get_json()
    text = data.get('text', '')
    prompt = f"Summarize this in simple points: {text}"
    answer = ask_gemini(prompt)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)