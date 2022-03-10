import os
import sqlite3

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
        self.conn = None
        self.c = None
        try:
            self.conn = sqlite3.connect(db_file)
            self.c = self.conn.cursor()
        except sqlite3.DatabaseError as e:
            print(e)

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
        self.c.execute(formatted)

    def add_tag(self, tag):
        params = tag.get_sql_tuple()
        self._execute_with_params("insert_tag.sql", params)
        self.conn.commit()

    def get_all_tags(self):
        result = self._execute_sql("get_all_tags.sql")
        tags = []
        for id, name in result:
            tags.append(Tag(id, name))
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

    def delete(self, table_name, key_name, key):
        self.c.execute("DELETE FROM %s WHERE %s = %s" %
                       (table_name, key_name, key))
        self.conn.commit()

    def close(self):
        self.conn.close()


def main():

    # create a database connection
    database = Database(DB_DIR)

    # create tables
    if database.conn is not None:
        script = "init_db.sql"
        database._execute_sql(script)

        at = Attempt(None, "2020-10-21", 10, 1.345, "text", 0.95, 1)
        ex = Exercise(None, "1", "2", "3", "4", "5")
        tag = Tag(None, "Today")

        database.add_attempt(at)
        database.add_tag(tag)
        database.add_exercise(ex)
        print(database.get_all_exercises())
        print(database.get_all_tags())
        print(database.get_all_attempts())
    else:
        print("Error! cannot create the database connection.")
