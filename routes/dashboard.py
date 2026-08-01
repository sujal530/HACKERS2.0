from flask import Blueprint, render_template, session, redirect, url_for
from database.db import get_db_connection

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        return redirect(url_for('auth.login'))

    user_id = session["user_id"]
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM progress WHERE user_id = %s", (user_id,))
    progress_data = cursor.fetchone()

    cursor.execute("SELECT * FROM roadmaps WHERE user_id = %s AND status = 'active' ORDER BY id DESC LIMIT 1", (user_id,))
    roadmap_data = cursor.fetchone()

    cursor.close()
    conn.close()

    dashboard_data = {
        "progress_percentage": progress_data['progress_percentage'] if progress_data else 0,
        "learning_streak": progress_data['learning_streak'] if progress_data else 0,
        "roadmap_title": roadmap_data['roadmap_title'] if roadmap_data else "No Active Roadmap"
    }

    return render_template('dashboard.html', dashboard_data=dashboard_data)