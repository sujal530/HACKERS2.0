from flask import Flask, redirect, url_for, session
from config import Config

from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.profile import profile_bp
from routes.roadmap import roadmap_bp

app = Flask(__name__)
app.config.from_object(Config)

# Register Blueprints for Phase 1
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(roadmap_bp)

@app.route('/')
def index():
    if "user_id" in session:
        return redirect(url_for('dashboard.dashboard'))
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)