from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Chatbot responses focused on AI topics
def chatbot_response(user_input):
    responses = {
        "what is ai": "AI stands for Artificial Intelligence. It enables machines to learn and make decisions.",
        "how does ai work": "AI works by using algorithms and data to make predictions and automate tasks.",
        "what are types of ai": "The main types of AI are Narrow AI, General AI, and Super AI.",
        "who invented ai": "AI as a field was founded in 1956 by researchers like John McCarthy and Alan Turing's work laid the foundation.",
        "what is machine learning": "Machine Learning is a subset of AI that allows computers to learn from data and improve performance without being explicitly programmed.",
        "bye": "Goodbye! Keep learning about AI!"
    }
    return responses.get(user_input.lower(), "I'm not sure about that. Can you ask something else related to AI?")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    bot_reply = chatbot_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)