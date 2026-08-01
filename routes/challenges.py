from flask import Blueprint, render_template, session, redirect, url_for
from flask import request, jsonify

from google import genai

from config import Config

from database.db import get_db_connection

client = genai.Client(api_key=Config.GEMINI_API_KEY)

challenges_bp = Blueprint("challenges", __name__)


@challenges_bp.route("/challenges")
def challenges():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM challenges")

    challenges = cursor.fetchall()

    conn.close()

    return render_template(

        "challenges.html",

        challenges=challenges

    )


@challenges_bp.route("/evaluate_challenge", methods=["POST"])
def evaluate():

    data = request.get_json()

    challenge_id = data["challenge_id"]

    answer = data["answer"]

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM challenges WHERE id=?",

        (challenge_id,)

    )

    challenge = cursor.fetchone()

    conn.close()

    prompt = f"""

You are an expert programming interviewer.

Challenge:

Title:
{challenge["title"]}

Description:
{challenge["description"]}

Student Answer:

{answer}

Evaluate the answer.

Return exactly in this format.

Score: X/10

Feedback:
Explain mistakes.
Suggest improvements.

XP:
Give XP between 0 and {challenge["xp"]}

"""

    response = client.models.generate_content(

        model="gemini-3.5-flash",

        contents=prompt

    )

    text = response.text

    score = 0
    xp = 0

    for line in text.splitlines():

        if line.startswith("Score:"):

            try:

                score = int(line.split(":")[1].split("/")[0].strip())

            except:

                score = 0

        if line.startswith("XP:"):

            try:

                xp = int(line.split(":")[1].strip())

            except:

                xp = 0

    return jsonify({

        "feedback": text,

        "score": score,

        "xp": xp

    })