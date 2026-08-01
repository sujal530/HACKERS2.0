CREATE DATABASE IF NOT EXISTS aspireai;
USE aspireai;

-- =====================================
-- USERS
-- =====================================

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- PROFILES
-- =====================================

CREATE TABLE IF NOT EXISTS profiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    career_goal VARCHAR(255) NOT NULL,
    skill_level VARCHAR(100) NOT NULL,
    interests TEXT,
    daily_available_time VARCHAR(50),
    learning_style VARCHAR(100),
    current_stage VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_profiles_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);

-- =====================================
-- ROADMAPS
-- =====================================

CREATE TABLE IF NOT EXISTS roadmaps (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    roadmap_title VARCHAR(255) NOT NULL,
    roadmap_json LONGTEXT,
    status VARCHAR(50) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_roadmaps_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);

-- =====================================
-- RESOURCES
-- =====================================

CREATE TABLE IF NOT EXISTS resources (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roadmap_id INT NOT NULL,
    topic VARCHAR(255) NOT NULL,
    youtube_link TEXT,
    documentation_link TEXT,
    github_link TEXT,
    article_link TEXT,
    book_link TEXT,
    difficulty VARCHAR(50),
    CONSTRAINT fk_resources_roadmap
        FOREIGN KEY (roadmap_id)
        REFERENCES roadmaps(id)
        ON DELETE CASCADE
);

-- =====================================
-- CHALLENGES
-- =====================================

CREATE TABLE IF NOT EXISTS challenges (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roadmap_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    difficulty VARCHAR(50),
    status VARCHAR(50) DEFAULT 'Pending',
    CONSTRAINT fk_challenges_roadmap
        FOREIGN KEY (roadmap_id)
        REFERENCES roadmaps(id)
        ON DELETE CASCADE
);

-- =====================================
-- PROGRESS
-- =====================================

CREATE TABLE IF NOT EXISTS progress (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    completed_topics INT DEFAULT 0,
    progress_percentage DECIMAL(5,2) DEFAULT 0.00,
    learning_streak INT DEFAULT 0,
    last_activity TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_progress_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);

-- =====================================
-- INDEXES
-- =====================================

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_profiles_user_id ON profiles(user_id);
CREATE INDEX idx_roadmaps_user_id ON roadmaps(user_id);
CREATE INDEX idx_resources_roadmap_id ON resources(roadmap_id);
CREATE INDEX idx_challenges_roadmap_id ON challenges(roadmap_id);
CREATE INDEX idx_progress_user_id ON progress(user_id);