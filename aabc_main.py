import mysql.connector
from PyQt5.QtWidgets import QApplication
from abc_a_first_window import FirstWindow

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dost0n1k"
)

cursor = db_connection.cursor()

database_name_to_check = 'library_management_pyqt_project'

check_query = f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{database_name_to_check}'"
cursor.execute(check_query)
result = cursor.fetchone()

tables = ["Books", "Users", "BookBorrowedUsers", "HistoryOfBooksUserBorrowed"]

books_table_query = f"""
    CREATE TABLE {tables[0]}
    (
        id INTEGER auto_increment,
        name VARCHAR (30),
        author VARCHAR (50),
        number_of_books INTEGER,
        number_of_books_available INTEGER,
        PRIMARY KEY (id)
    );
"""

users_table_query = f"""
    CREATE TABLE {tables[1]}
    (
        id INTEGER auto_increment,
        passport_serial VARCHAR (2),
        passport_serial_number VARCHAR (7),
        full_name VARCHAR (50),
        age INTEGER (3),
        number_of_borrowed_books INTEGER,
        path_to_user_s_pic VARCHAR (150),
        PRIMARY KEY (id)
    );
"""

borrowed_users_query = f"""
    CREATE TABLE {tables[2]}
    (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        book_id INTEGER,
        borrow_date VARCHAR (19),
        return_date VARCHAR (19),
        returned INTEGER (1),
        penalty INTEGER,
        penalty_is_paid INTEGER(1),
        FOREIGN KEY (user_id) REFERENCES {tables[1]}(id),
        FOREIGN KEY (book_id) REFERENCES {tables[0]}(id)
    );
"""

history_of_borrows_query = f"""
    CREATE TABLE {tables[3]}
    (
        user_id INTEGER,
        book_id INTEGER,
        borrowed_day INTEGER,
        returned_day INTEGER,
        penalty INTEGER,
        penalty_is_paid INTEGER,
        FOREIGN KEY (user_id) REFERENCES {tables[1]}(id),
        FOREIGN KEY (book_id) REFERENCES {tables[0]}(id),
        FOREIGN KEY (borrowed_day) REFERENCES {tables[2]}(id),
        FOREIGN KEY (returned_day) REFERENCES {tables[2]}(id),
        FOREIGN KEY (penalty) REFERENCES {tables[2]}(id),
        FOREIGN KEY (penalty_is_paid) REFERENCES {tables[2]}(id)
    );
"""

use_query = f"USE {database_name_to_check};"
cursor.execute(use_query)
if not result:
    create_database_query = f"CREATE DATABASE {database_name_to_check};"
    cursor.execute(create_database_query)
    table_creation_queries = [books_table_query, users_table_query, borrowed_users_query, history_of_borrows_query]
    for query in table_creation_queries:
        cursor.execute(query)

db_connection.commit()

_____name_of_library = "Minnie Muse"

application = QApplication([])

__first_window = FirstWindow(_____name_of_library)
__first_window.show()

application.exec()

cursor.close()
db_connection.close()
