from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from database.db import get_db_connection

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET', 'POST'], endpoint='view_profile')
def view_profile():
    if "user_id" not in session:
        return redirect(url_for('auth.login'))

    user_id = session["user_id"]
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        career_goal = request.form.get('career_goal')
        skill_level = request.form.get('skill_level')
        interests = request.form.get('interests')
        daily_available_time = request.form.get('daily_available_time')
        learning_style = request.form.get('learning_style')

        cursor.execute("SELECT id FROM profiles WHERE user_id = ?", (user_id,))
        existing_profile = cursor.fetchone()

        if existing_profile:
            cursor.execute("""
                UPDATE profiles 
                SET career_goal=?, skill_level=?, interests=?, daily_available_time=?, learning_style=? 
                WHERE user_id=?
            """, (career_goal, skill_level, interests, daily_available_time, learning_style, user_id))
        else:
            cursor.execute("""
                INSERT INTO profiles (user_id, career_goal, skill_level, interests, daily_available_time, learning_style) 
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, career_goal, skill_level, interests, daily_available_time, learning_style))

        conn.commit()
        flash("Profile updated successfully!", "success")

    cursor.execute("SELECT * FROM profiles WHERE user_id = ?", (user_id,))
    profile_data = cursor.fetchone()
    if profile_data:
        profile_data = dict(profile_data)

    # Make sure this return statement is INSIDE def view_profile():
    return render_template('profile.html', profile_data=profile_data)