import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.DatabaseError as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.DataError as e:
        print(e)


def main():
    database = "..data/Copyclare.db"

    exercise_table = """ CREATE TABLE IF NOT EXISTS exercises(
                            name TEXT PRIMARY KEY UNIQUE,
                            video_directory TEXT,
                            image_directory TEXT,
                            descriptions TEXT
                        ); """

    attempt_table = """CREATE TABLE IF NOT EXISTS attempt(
                            date TEXT PRIMARY KEY UNIQUE,
                            nums_of_repetition INTEGER,
                            duration REAL,
                            accuracy REAL,
                            FOREIGN KEY (user_name) REFERENCES user (name),
                            FOREIGN KEY (exercise_name TEXT) REFERENCES exercises (name)
                        );"""

    user_table= """ CREATE TABLE IF NOT EXISTS user(
                        name TEXT PRIMARY KEY UNIQUE,
                        age INTEGER
                    ); """


    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create exercises table
        create_table(conn, exercise_table)

        # create attempt table
        create_table(conn, attempt_table)

        # create user table
        create_table(conn, user_table)
    else:
        print("Error! cannot create the database connection.")


