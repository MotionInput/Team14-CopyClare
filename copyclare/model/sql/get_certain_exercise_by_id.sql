SELECT exercise_id, exercise_name, video_directory, image_directory,
        description, angles_json FROM exercises WHERE exercise_id = %d; 