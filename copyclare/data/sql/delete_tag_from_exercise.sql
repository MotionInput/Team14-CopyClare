--Contributors: Adi Bozzhanov

DELETE FROM tag_to_exercise
WHERE tag_name='%s'
AND exercise_id=%s;
