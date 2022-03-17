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
       tag_name TEXT NOT NULL UNIQUE,
       PRIMARY KEY (tag_name)
);

-- Transition table to allow many to many relationship between tags and exercises

CREATE TABLE IF NOT EXISTS tag_to_exercise(
       tag_name TEXT,
       exercise_id INTEGER,
       FOREIGN KEY (tag_name) REFERENCES tags (tag_name),
       FOREIGN KEY (exercise_id) REFERENCES exercises (exercise_id),
       CONSTRAINT PK_tag_to_exercise PRIMARY KEY (tag_name, exercise_id)
);

-- Creating attempts table

CREATE TABLE IF NOT EXISTS attempts(
       attempt_id INTEGER NOT NULL UNIQUE,
       attempt_date TEXT,
       num_of_repetitions INTEGER,
       duration REAL,
       session_json TEXT,
       accuracy REAL,
       heatmap TEXT,
       exercise_id INTEGER,
       PRIMARY KEY (attempt_id AUTOINCREMENT),
       FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id)
);
