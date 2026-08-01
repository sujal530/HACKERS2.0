import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "aspire_ai.db")


def get_db_connection():
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

    # ---------------- PROFILES ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,

        career_goal TEXT,

        skill_level TEXT,

        interests TEXT,

        daily_available_time TEXT,

        learning_style TEXT,

        FOREIGN KEY(user_id) REFERENCES users(id)

    )
    """)

    # ---------------- ROADMAP ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roadmaps(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,

        roadmap_title TEXT DEFAULT 'No Active Roadmap',

        status TEXT DEFAULT 'active',

        FOREIGN KEY(user_id) REFERENCES users(id)

    )
    """)

    # ---------------- PROGRESS ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progress(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,

        progress_percentage REAL DEFAULT 0,

        learning_streak INTEGER DEFAULT 0,

        FOREIGN KEY(user_id) REFERENCES users(id)

    )
    """)

    # ---------------- CHALLENGES ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS challenges(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT NOT NULL,

        description TEXT NOT NULL,

        difficulty TEXT NOT NULL,

        category TEXT NOT NULL,

        xp INTEGER NOT NULL

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

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(user_id) REFERENCES users(id),

        FOREIGN KEY(challenge_id) REFERENCES challenges(id)

    )
    """)

    # ---------------- INSERT SAMPLE CHALLENGES ----------------

    cursor.execute("SELECT COUNT(*) FROM challenges")

    count = cursor.fetchone()[0]

    if count == 0:

        cursor.executemany("""

        INSERT INTO challenges
        (title,description,difficulty,category,xp)

        VALUES (?,?,?,?,?)

        """, [

            (

                "Second Largest Number",

                "Write a Python function that returns the second largest number from a list.",

                "Easy",

                "Python",

                50

            ),

            (

                "Palindrome",

                "Write a Python function to check whether a string is palindrome.",

                "Easy",

                "Python",

                40

            ),

            (

                "Binary Search",

                "Implement Binary Search in Python.",

                "Medium",

                "DSA",

                100

            ),

            (

                "Second Highest Salary",

                "Write an SQL query to find the second highest salary.",

                "Medium",

                "SQL",

                80

            ),

            (

                "Flask Login System",

                "Create a login authentication system using Flask.",

                "Hard",

                "Web Development",

                150

            )

        ])

    conn.commit()

    conn.close()

    print("Database initialized successfully.")