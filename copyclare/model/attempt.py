from copyclare.model.user import user


class Attempt:
    def __init__(self,date,numsOFrepetition,duration,accuracy,user_name,exerceise_name):
        self.date = date
        self.nums_of_repetiton = numsOFrepetition
        self.duration = duration
        self.accuracy = accuracy
        self.user_name = user_name
        self.exercise_name = exerceise_name
 