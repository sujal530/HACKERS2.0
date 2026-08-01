from flask import Flask, redirect, url_for, session
from config import Config
from database.db import init_db
# Blueprints
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.profile import profile_bp
from routes.roadmap import roadmap_bp
from routes.mentor import mentor_bp
from routes.ai import ai_bp
from routes.challenges import challenges_bp

app = Flask(__name__)
app.config.from_object(Config)
init_db()

# Secret Key
app.secret_key = Config.SECRET_KEY

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
app.register_blueprint(profile_bp, url_prefix="/profile")
app.register_blueprint(roadmap_bp, url_prefix="/roadmap")
app.register_blueprint(mentor_bp)
app.register_blueprint(ai_bp)
app.register_blueprint(challenges_bp)

# Home Route
@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("dashboard.dashboard"))
    return redirect(url_for("auth.login"))

# Test Route
@app.route("/test")
def test():
    return {
        "logged_in": "user_id" in session,
        "user": session.get("user_name")
    }

if __name__ == "__main__":
    app.run(debug=True)