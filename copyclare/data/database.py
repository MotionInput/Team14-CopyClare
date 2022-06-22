"""
Contributors: Adi Bozzhanov, Sree Sanakkayala, Tianhao Chen

"""
"""
database.py

copyclare.data.Database

Our database module that provides and interface to our SQLITE database

This module allows executing sctipts that are defined in a sql directory

you can reference sql directory in the code by using ``SQL_DIR``.

.. code-block:: python

   # sample usage:
   from copyclare.data import SQL_DIR

   # SQL_DIR is a string containing the absulute path to our SQL queries.
"""




import json
import os
import pathlib
import sqlite3
from distutils.dir_util import copy_tree
from copyclare.data import DATA_DIR, DB_DIR, SQL_DIR
from copyclare.data.objects import Attempt, Exercise, Tag
from copyclare.model.accuracy_v2 import AccuracyModel
class Database:
    def __init__(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """

        if not os.path.exists(os.path.join(DATA_DIR, "videos")) or not os.path.exists(os.path.join(DATA_DIR, "images")):
            print("Initialising usesr data directory")
            os.makedirs(DATA_DIR, exist_ok=True)
            local_data = pathlib.Path(__file__).parent.parent.parent.joinpath("data")
            copy_tree(local_data, DATA_DIR)

        if not os.path.exists(os.path.join(DATA_DIR, "progress-charts")):
            os.makedirs(os.path.join(DATA_DIR, "progress-charts"))
        
        if not os.path.exists(os.path.join(DATA_DIR, "accuracy-graphs")):
            os.makedirs(os.path.join(DATA_DIR, "accuracy-graphs"))

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

        # with open(DATA_DIR + "/test/1.json", "r") as f:
        #     json1 = f.read()
        # with open(DATA_DIR + "/test/2.json", "r") as f:
        #     json2 = f.read()
        # with open(DATA_DIR + "/test/3.json", "r") as f:
        #     json3 = f.read()

        # with open(DATA_DIR + "/videos/clare1.txt", "r", encoding="UTF-8") as f:
        #    clare1_desc = f.read()
        with open(DATA_DIR + "/videos/clare2.txt", "r", encoding="UTF-8") as f:
            clare2_desc = f.read()
        # with open(DATA_DIR + "/videos/clare3.txt", "r", encoding="UTF-8") as f:
        #    clare3_desc = f.read()

        exercise = Exercise(None, "Shoulder Rotation", "/videos/clare2.mp4",
                            "/images/1.png", clare2_desc, "-1")
        joints = [
            "left_elbow", "left_shoulder", "right_elbow", "right_shoulder"
        ]
        accuracymodel = AccuracyModel(exercise, joints)
        exercise.angles_json = json.dumps(
            accuracymodel.get_angles(DATA_DIR + exercise.video_directory))
        self.add_exercise(exercise)

        for tag in tags:
            self.add_tag(tag)

        t = Tag("My Exercises")

        exercises = self.get_all_exercises()
        self.add_tag_to_exercise(t, exercises[0])

    def _file_to_commands(self, sql_path):
        """
        Given a file name of the script file
        returns a list of string representations
        of all commands

        the script MUST be in the sql directory
        """
        path = SQL_DIR + sql_path
        print(path)
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
            pass
        else:
            self.conn.commit()

    def remove_tag_from_exercise(self, tag, exercise):
        tag_name = tag.tag_name
        ex_id = exercise.id
        params = (tag_name, ex_id)

        self._execute_with_params("delete_tag_from_exercise.sql", params)

    def add_tag_to_exercise(self, tag, exercise):

        self.add_tag(tag)
        t_name = tag.tag_name
        e_id = exercise.id
        try:
            self._execute_with_params("insert_tags_to_exercise.sql",
                                      (t_name, e_id))
        except sqlite3.IntegrityError as err:
            pass
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

        for p1, p2, p3, p4, p5, p6, p7 in result:
            attempts.append(Attempt(p1, p2, p3, p4, p5, p6, p7))

        return attempts

    def get_one_attempt_by_ID(self, id):
        result = self._execute_with_params("get_certain_attempt_by_id.sql", id)
        for p1, p2, p3, p4, p5, p6, p7 in result:
            return Attempt(p1, p2, p3, p4, p5, p6, p7)

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

    t = Tag("My Exercises")
    ex = database.get_one_exercise_by_ID(1)

    ts = database.get_exercise_tags(ex)

    print(t)
    print(ex)
    print(ts)

    database.remove_tag_from_exercise(t, ex)

    ts = database.get_exercise_tags(ex)

    print(ts)

    return database
