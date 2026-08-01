CREATE DATABASE IF NOT EXISTS aspire_ai;
USE aspire_ai;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS profiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    target_role VARCHAR(100),
    current_skills TEXT,
    experience_level VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS challenges (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,

    description TEXT NOT NULL,

    difficulty TEXT NOT NULL,

    category TEXT NOT NULL,

    xp INTEGER NOT NULL

);

CREATE TABLE IF NOT EXISTS challenge_progress (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    challenge_id INTEGER,

    answer TEXT,

    ai_feedback TEXT,

    score INTEGER,

    xp_earned INTEGER DEFAULT 0,

    completed INTEGER DEFAULT 0,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

INSERT INTO challenges(title,description,difficulty,category,xp)
VALUES
('Second Largest Number',
'Write a Python function that returns the second largest number from a list.',
'Easy',
'Python',
50),

('Palindrome',
'Write a function to check whether a string is palindrome.',
'Easy',
'Python',
40),

('Binary Search',
'Implement Binary Search.',
'Medium',
'DSA',
100),

('SQL Employee',
'Write SQL query to find second highest salary.',
'Medium',
'SQL',
80),

('Flask Login',
'Create a login authentication route using Flask.',
'Hard',
'Web Development',
150);