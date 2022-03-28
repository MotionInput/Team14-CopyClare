INSERT INTO attempts (
       attempt_date,
       num_of_repetitions,
       duration,
       session_json,
       accuracy,
       exercise_id
)
VALUES ( '%s', %d, %f, '%s', %f, %d);
