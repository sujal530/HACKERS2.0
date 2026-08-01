from flask import Blueprint, render_template, session, redirect, url_for
from database.db import get_db_connection

roadmap_bp = Blueprint('roadmap', __name__)

@roadmap_bp.route('/roadmap')
def roadmap():
    if "user_id" not in session:
        return redirect(url_for('auth.login'))

    user_id = session["user_id"]
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM roadmaps WHERE user_id = %s AND status = 'active' ORDER BY id DESC LIMIT 1", (user_id,))
    roadmap_data = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template('roadmap.html', roadmap_data=roadmap_data)