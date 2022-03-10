-- Exercises table

CREATE TABLE IF NOT EXISTS exercises(
       exercise_id INTEGER NOT NULL UNIQUE,
       exercise_name TEXT,
       video_directory TEXT,
       image_directory TEXT,
       description TEXT,
       angles_json TEXT,
       PRIMARY KEY (exercise_id AUTOINCREMENT)
);

-- Tags table storing stuff like Today's

CREATE TABLE IF NOT EXISTS tags(
       tag_id INTEGER NOT NULL UNIQUE,
       tag_name TEXT,
       PRIMARY KEY (tag_id AUTOINCREMENT)
);

-- Transition table to allow many to many relationship between tags and exercises

CREATE TABLE IF NOT EXISTS tag_to_exercise(
       tag_id INTEGER,
       exercise_id INTEGER,
       FOREIGN KEY (tag_id) REFERENCES tags (tag_id),
       FOREIGN KEY (exercise_id) REFERENCES exercises (exercise_id),
       CONSTRAINT PK_tag_to_exercise PRIMARY KEY (tag_id, exercise_id)
);

-- Creating attempts table

CREATE TABLE IF NOT EXISTS attempts(
       attempt_id INTEGER NOT NULL UNIQUE,
       attempt_date TEXT,
       num_of_repetitions INTEGER,
       duration REAL,
       session_json TEXT,
       accuracy REAL,
       exercise_id INTEGER,
       PRIMARY KEY (attempt_id AUTOINCREMENT),
       FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id)
);
