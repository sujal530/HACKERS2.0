from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database.db import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        current_user = cursor.fetchone()
        cursor.close()
        conn.close()

        if current_user and check_password_hash(current_user['password'], password):
            session["user_id"] = current_user['id']
            session["user_name"] = current_user['full_name']
            return redirect(url_for('dashboard.dashboard'))
        else:
            flash("Invalid credentials", "danger")

    return render_template('login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        password = generate_password_hash(request.form.get('password'))

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (full_name, email, password) VALUES (%s, %s, %s)", 
                           (full_name, email, password))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('auth.login'))
        except Exception:
            conn.rollback()
            cursor.close()
            conn.close()
            flash("Email already exists or database error.", "danger")

    return render_template('signup.html')

@auth_bp.route('/logout')
def logout():
    session.pop("user_id", None)
    session.pop("user_name", None)
    return redirect(url_for('auth.login'))