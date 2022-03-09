import sqlite3

from copyclare.model.attempt import Attempt
from copyclare.model.exercises import Exercise
from copyclare.model.user import User
from copyclare import DATA_PATH


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
            self.c.execute("PRAGMA FOREIGN_KEYS = ON")
            self.c.execute("PRAGMA foreign_keys")
            self.c.fetchone()
        except sqlite3.DatabaseError as e:
            print(e)

    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            self.c.execute(create_table_sql)
        except sqlite3.DataError as e:
            print(e)

    def init_user(self, name):
        cursor = self.c.execute("INSERT INTO user (name,age) \
                                VALUE (%s)" % (name))
        self.conn.commit()
        user = User(name)
        return user

    def add_exercise(self, exercise):
        # input an exercise object and keep it in the database
        cursor = self.c.execute(
            "INSERT INTO exercises (name, video_directory, image_directory, descriptions, category, angle_over_time) \
                                VALUE (%s,%s,%s,%s,%s,%s)" %
            (exercise.name, exercise.video_directory, exercise.image_directory,
             exercise.descriptions, exercise.category, exercise.AngleOverTime))
        self.conn.commit()

    def get_exercises(self, key_type, key):
        # use the data here to get exercise instances
        if key_type == "all":
            cursor = self.c.execute(
                "SELECT exercise_name, video_directory, image_directory, descriptions, category, angle_over_time FROM exercises"
            )
        else:
            cursor = self.c.execute(
                "SELECT exercise_name, video_directory, image_directory, descriptions, category, angle_over_time FROM exercises WHERE %s = %s"
            ) % (key_type, key)
        exercises = []
        for row in cursor:
            exercise = Exercise(row[0], row[1], row[2], row[3], row[4], row[5])
            exercises.append(exercise)
        return exercises

    """def get_exercise(self,exercise_name = None):
        # use the data here to create a new exercise instance
        if exercise_name == None:
            cursor = self.c.execute("SELECT video_directory, image_directory, descriptions, category, angle_over_time FROM exercises WHERE name = %s") %(exercise_name)
            for row in cursor:
                exercise = Exercise(exercise_name,row[0],row[1],row[2],row[3],row[4])
                return exercise
        else:
            cursor = self.c.execute("SELECT exercise_name, video_directory, image_directory, descriptions, category, angle_over_time FROM exercises")
            exercises = []
            for row in cursor:
                exercise = Exercise(row[0],row[1],row[2],row[3],row[4],row[5])
                exercises.append(exercise)
            return exercises
        print("can not find the corresponding exercise")
        return None"""

    def get_all_categories(self):
        # return a list of name of categories
        cursor = self.c.execute("SELECT category FROM exercises")
        categories = []
        for row in cursor:
            if row[0] not in categories:
                categories.append(row[0])
        return categories

    def add_attempt(self, date, nums_of_repetition, duration, accuracy,
                    user_name, exercise_name):
        self.c.execute(
            "INSERT INTO attempts (date,nums_of_repition,duration,accuracy,user_name,exercise_name) \
                                            VALUE (%s,%d,%f,%f,%s,%s)" %
            (date, nums_of_repetition, duration, accuracy, user_name,
             exercise_name))
        self.conn.commit()

    def get_attempts_in_past(self, date1, date2=None):
        # return all attempt instances whose date is between the two given dates in a list
        attempts = []
        cursor = self.c.execute(
            "SELETE date nums_of_retetition duration accuracy user_name exercise_name FROM attempts WHERE date BETWEEN %s AND %s"
            % (date1, date2))
        for row in cursor:
            attempt = Attempt(row[0], row[1], row[2], row[3], row[4], row[5])
            attempts.append(attempt)
        return attempts

    def delete(self, table_name, key_name, key):
        self.c.execute("DELETE FROM %s WHERE %s = %s" %
                       (table_name, key_name, key))
        self.conn.commit()

    def close(self):
        self.conn.close()


def main():
    database_directory = DATA_PATH + "/Copyclare.db"

    exercises_table = """ CREATE TABLE IF NOT EXISTS exercises(
                            name TEXT PRIMARY KEY UNIQUE,
                            video_directory TEXT,
                            image_directory TEXT,
                            descriptions TEXT,
                            category TEXT,
                            angle_over_time TEXT
                        ); """

    attempts_table = """CREATE TABLE IF NOT EXISTS attempts(
                            date TEXT PRIMARY KEY UNIQUE,
                            nums_of_repetition INTEGER,
                            duration REAL,
                            accuracy REAL,
                            user_name TEXT,
                            exercise_name TEXT,
                            FOREIGN KEY (user_name) REFERENCES user (name),
                            FOREIGN KEY (exercise_name) REFERENCES exercises (name)
                        );"""

    user_table = """ CREATE TABLE IF NOT EXISTS user(
                        name TEXT PRIMARY KEY UNIQUE,
                        age INTEGER
                    ); """

    # create a database connection
    database = Database(database_directory)

    # create tables
    if database.conn is not None:
        # create exercises table
        database.create_table(exercises_table)

        # create attempt table
        database.create_table(user_table)

        # create user table
        database.create_table(attempts_table)
    else:
        print("Error! cannot create the database connection.")
