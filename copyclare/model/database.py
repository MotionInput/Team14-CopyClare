import os
import sqlite3
import json
from unittest import result

from copyclare.model.attempt import Attempt
from copyclare.model.exercises import Exercise
from copyclare.model.tag import Tag
from copyclare import DATA_PATH

SQL_DIR = os.path.dirname(os.path.realpath(__file__)) + "/sql/"
DB_DIR = DATA_PATH + "/Copyclare.db"


class Database:
    def __init__(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """

        exists = os.path.exists(db_file)
        self.conn = None
        self.c = None
        try:
            self.conn = sqlite3.connect(db_file)
            self.c = self.conn.cursor()
        except sqlite3.DatabaseError as e:
            print(e)

        if not exists:
            print("Database not found, creating and populating a new one")
            self._execute_sql("init_db.sql")
            self._init_debug_data()
            self.conn.commit()
        else:
            print("Database exists")

    def _init_debug_data(self):

        tags = [
            Tag("My Exercises"),
        ]

        with open(DATA_PATH + "/test/1.json", "r") as f:
            json1 = f.read()
        with open(DATA_PATH + "/test/2.json", "r") as f:
            json2 = f.read()
        with open(DATA_PATH + "/test/3.json", "r") as f:
            json3 = f.read()

        with open(DATA_PATH + "/videos/clare1.txt", "r") as f:
            clare1_desc = f.read()
        with open(DATA_PATH + "/videos/clare2.txt", "r") as f:
            clare2_desc = f.read()
        with open(DATA_PATH + "/videos/clare3.txt", "r") as f:
            clare3_desc = f.read()

        exercises = [
            Exercise(
                None,
                "Push-ups against a wall",
                "/videos/clare1.mp4",
                "null",
                clare1_desc,
                json1,
            ),
            Exercise(
                None,
                "Shoulder Rotation",
                "/videos/clare2.mp4",
                "null",
                clare2_desc,
                json2,
            ),
            Exercise(
                None,
                "Wall Slide",
                "/videos/clare3.mp4",
                "null",
                clare3_desc,
                json3,
            ),
        ]

        for tag in tags:
            self.add_tag(tag)

        for ex in exercises:
            self.add_exercise(ex)

        t = Tag("My Exercises")

        exercises = self.get_all_exercises()
        self.add_tag_to_exercise(t, exercises[0])
        self.add_tag_to_exercise(t, exercises[1])

    def _file_to_commands(self, sql_path):
        """
        Given a file name of the script file
        returns a list of string representations
        of all commands

        the script MUST be in the sql directory
        """
        path = SQL_DIR + sql_path
        with open(path, "r") as scripts:
            text = "".join(scripts.readlines())
            commands = [
                each for each in text.split(";") if len(each.strip()) > 0
            ]
        return commands

    def _execute_sql(self, sql_path):
        """
        The script file can have more that 1 command

        Will return results of the last ran command
        """
        commands = self._file_to_commands(sql_path)
        for com in commands:
            self.c.execute(com)

        return [row for row in self.c]

    def _execute_with_params(self, sql_path, params):
        """
        This function will only execute the first
        command from the script file.
        """

        command = self._file_to_commands(sql_path)[0]
        formatted = command % params
        # print(formatted)
        self.c.execute(formatted)
        return [row for row in self.c]

    def add_tag(self, tag):
        params = tag.get_sql_tuple()
        try:
            self._execute_with_params("insert_tag.sql", params)
        except sqlite3.IntegrityError as err:  # tag already exists
            print(f"Tag '{tag.tag_name}' already exists")
        else:
            self.conn.commit()

    def add_tag_to_exercise(self, tag, exercise):

        self.add_tag(tag)
        t_name = tag.tag_name
        e_id = exercise.id
        try:
            self._execute_with_params("insert_tags_to_exercise.sql",
                                      (t_name, e_id))
        except sqlite3.IntegrityError as err:
            print(f"Excercise already has tag '{t_name}'")
        self.conn.commit()

    def get_exercise_tags(self, exercise):
        """
        Given the exercise id returns a list of tag objects
        """
        e_id = exercise.id

        result = self._execute_with_params("get_exercise_tags.sql", e_id)
        tags = [Tag(each[0]) for each in result]

        return tags

    def get_all_tags(self):
        result = self._execute_sql("get_all_tags.sql")
        tags = []
        for name, in result:
            tags.append(Tag(name))
        return tags

    def add_exercise(self, exercise):
        # input an exercise object and keep it in the database
        # TODO: add code to also add the tags of the exercise
        params = exercise.get_sql_tuple()
        self._execute_with_params("insert_exercise.sql", params)
        self.conn.commit()

    def get_all_exercises(self):
        """
        Returns a list of all exercise objects
        """

        result = self._execute_sql("get_all_exercises.sql")
        exercises = []
        for p1, p2, p3, p4, p5, p6 in result:
            exercises.append(Exercise(p1, p2, p3, p4, p5, p6))

        return exercises

    def get_exercises_by_tag(self, tag):

        result = self._execute_with_params("get_exercises_by_tag.sql",
                                           tag.get_sql_tuple())
        exercises = []
        for p1, p2, p3, p4, p5, p6 in result:
            exercises.append(Exercise(p1, p2, p3, p4, p5, p6))

        return exercises

    def get_one_exercise_by_ID(self, id):
        result = self._execute_with_params("get_certain_exercise_by_id.sql",
                                           id)
        for p1, p2, p3, p4, p5, p6 in result:
            return Exercise(p1, p2, p3, p4, p5, p6)

    def add_attempt(self, attempt):

        params = attempt.get_sql_tuple()
        self._execute_with_params("insert_attempt.sql", params)
        self.conn.commit()

    def get_all_attempts(self):

        result = self._execute_sql("get_all_attempts.sql")
        attempts = []

        for p1, p2, p3, p4, p5, p6, p7, p8 in result:
            attempts.append(Attempt(p1, p2, p3, p4, p5, p6, p7, p8))

        return attempts

    def get_one_attempt_by_ID(self, id):
        result = self._execute_with_params("get_certain_attempt_by_id.sql", id)
        for p1, p2, p3, p4, p5, p6, p7, p8 in result:
            return Attempt(p1, p2, p3, p4, p5, p6, p7, p8)    

    def get_attempt_in_exercise(self):
        exercises = [[]]
        attempts = self.get_all_attempts()
        for attempt in attempts:
            flag = False
            for exe in exercises:
                if len(exe) == 0:
                    exe.append(attempt)
                    flag = True
                elif exe[0].exercise_id == attempt.exercise_id:
                    exe.append(attempt)
                    flag = True
            if flag == False:
                exercises.append([attempt])

        return exercises            


    def get_exercise_name_and_desc_by_ID(self, id):
        exercise = self.get_one_exercise_by_ID(id)
        return exercise.name, exercise.description

    def delete(self, table_name, key_name, key):
        self.c.execute("DELETE FROM %s WHERE %s = %s" %
                       (table_name, key_name, key))
        self.conn.commit()

    def close(self):
        self.conn.close()


def main():

    # create a database connection
    database = Database(DB_DIR)
    return database
