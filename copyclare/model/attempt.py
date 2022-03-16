class Attempt:
    def __init__(self, id, date, num_of_repetitons, duration, session_json,
                 accuracy, heatmap, exercise_id):
        self.id = id
        self.date = date
        self.num_of_repetitons = num_of_repetitons
        self.duration = duration
        self.session_json = session_json
        self.accuracy = accuracy
        self.heatmap = heatmap
        self.exercise_id = exercise_id

    def __repr__(self):
        return f"<Attempt[{self.id}]: {self.exercise_id}, {self.date}>"

    def get_sql_tuple(self):
        return (self.date, self.num_of_repetitons, self.duration,
                self.session_json, self.accuracy, self.heatmap, self.exercise_id)
