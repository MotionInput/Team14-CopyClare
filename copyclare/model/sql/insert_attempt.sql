INSERT INTO attempts (
       attempt_date,
       num_of_repetitions,
       duration,
       session_json,
       accuracy,
       heatmap,
       exercise_id
)
VALUES ( '%s', %d, %f, '%s', %f, '%s', %d);
