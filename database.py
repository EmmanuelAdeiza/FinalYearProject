
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM task")

    rows = cur.fetchall()
    counter = 0
    for row in rows:
        counter += 1
    print(counter)

def main():
    database = "C:\\Users\EmmaAdeiza\PycharmProjects\FinalYearProject\ProjectDatabase.db"

    # create a database connection
    conn = create_connection(database)
    conn.execute('''CREATE TABLE task
    (ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    TYPE TEXT NOT NULL,
    SIZE TEXT NOT NULL,
    DATE_ACCESSED TEXT NOT NULL,
    ANALYSED BOOL NOT NULL)
    ''')

    with conn:
        print("2. Query all tasks")
        select_all_tasks(conn)


if __name__ == '__main__':
    main()