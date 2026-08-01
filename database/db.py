import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "aspire_ai.db")

def get_db_connection():
    print("DATABASE PATH:", os.path.abspath(DB_PATH))
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():

    conn = get_db_connection()

    cursor = conn.cursor()

    # ---------------- USERS ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
    """)

    # ---------------- PROFILE ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    career_goal TEXT,
    skill_level TEXT,
    interests TEXT,
    daily_available_time TEXT,
    learning_style TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
    """)

    # ---------------- ROADMAP ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roadmaps(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        roadmap_title TEXT,

        status TEXT

    )
    """)

    # ---------------- PROGRESS ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progress(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        progress_percentage INTEGER DEFAULT 0,

        learning_streak INTEGER DEFAULT 0

    )
    """)

    # ---------------- CHALLENGES ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS challenges(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT,

        description TEXT,

        difficulty TEXT,

        category TEXT,

        xp INTEGER

    )
    """)

    # ---------------- CHALLENGE PROGRESS ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS challenge_progress(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        challenge_id INTEGER,

        answer TEXT,

        ai_feedback TEXT,

        score INTEGER,

        xp_earned INTEGER DEFAULT 0,

        completed INTEGER DEFAULT 0,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)
    
    # ---------------- RESOURCES ----------------

   

    conn.commit()

    conn.close()