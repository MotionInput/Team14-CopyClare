class Exercise:
    def __init__(self, id, exercise_name, video_directory, image_directory,
                 description, angles_json):
        self.id = id
        self.name = exercise_name
        self.video_directory = video_directory
        self.image_directory = image_directory
        self.description = description
        self.angles_json = angles_json

    def __repr__(self):
        return f"<Exercise[{self.id}]: {self.name}>"

    def get_sql_tuple(self):
        return (self.name, self.video_directory, self.image_directory,
                self.description, self.angles_json)
