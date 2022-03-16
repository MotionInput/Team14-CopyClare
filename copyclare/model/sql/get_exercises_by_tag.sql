SELECT *
FROM exercises
WHERE exercise_id in (
      SELECT exercise_id
      FROM tag_to_exercise
      WHERE tag_name = '%s'
)
