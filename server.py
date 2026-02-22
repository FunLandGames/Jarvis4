from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# Groq API key as environment variable
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')

    if not question:
        return jsonify({"answer": "Please type a question!"})

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": question,
        "max_tokens": 150
    }

    response = requests.post("https://api.groq.com/v1/queries", headers=headers, json=payload)
    
    if response.status_code != 200:
        return jsonify({"answer": "Failed to get response from Groq API."})

    answer = response.json().get('answer', 'No answer found.')
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
