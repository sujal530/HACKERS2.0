from flask import Blueprint, request, jsonify, session
from google import genai
from config import Config

ai_bp = Blueprint("ai", __name__)

client = genai.Client(api_key=Config.GEMINI_API_KEY)

# Store conversation history for current server session
chat_history = {}


@ai_bp.route("/ask_ai", methods=["POST"])
def ask_ai():
    try:
        data = request.get_json()

        question = data.get("question", "").strip()

        if question == "":
            return jsonify({
                "success": False,
                "answer": "Please enter a question."
            })

        user_id = session.get("user_id", "guest")

        if user_id not in chat_history:
            chat_history[user_id] = []

        # Save user message
        chat_history[user_id].append({
            "role": "user",
            "text": question
        })

        # Keep last 10 messages
        history = chat_history[user_id][-10:]

        prompt = """
You are AspireAI.

You are NOT ChatGPT.

You are a Personal AI Growth Mentor.

Rules:

- Answer only what the user asks.
- Never introduce yourself unless asked.
- Keep responses clean and professional.
- If user asks programming, provide working code.
- If user asks theory, explain simply.
- Use bullet points when useful.
- Format code inside markdown.
- Do not ask unnecessary questions.
- If greeted, reply naturally in one sentence.

Conversation:
"""

        for message in history:
            prompt += f"\n{message['role']}: {message['text']}"

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        answer = response.text

        chat_history[user_id].append({
            "role": "assistant",
            "text": answer
        })

        return jsonify({
            "success": True,
            "answer": answer
        })

    except Exception as e:

        print(e)

        return jsonify({
            "success": False,
            "answer": str(e)
        }), 500


@ai_bp.route("/clear_chat", methods=["POST"])
def clear_chat():

    user_id = session.get("user_id", "guest")

    chat_history[user_id] = []

    return jsonify({
        "success": True
    })