import mysql.connector
from PyQt5.QtWidgets import QApplication

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

if result:
    use_query = f"USE {database_name_to_check};"
    cursor.execute(use_query)
else:
    create_database = f"CREATE DATABASE {database_name_to_check};"
    cursor.execute(create_database)
    use_query = f"USE {database_name_to_check};"
    cursor.execute(use_query)
    
    tables = ["Books", "Users", "BookBorrowedUsers", "HistoryOfBooksUserBorrowed"]

    books_table = f"""
                        CREATE TABLE {tables[0]}
                        (
                            id INTEGER auto_increment,
                            name VARCHAR (30),
                            author VARCHAR (50),
                            number_of_books INTEGER,
                            number_of_books_available INTEGER,
                            PRIMARY KEY (id)
                        );"""
                        
    users_table = f"""
                    CREATE TABLE {tables[1]}
                    (
                        id INTEGER auto_increment,
                        full_name VARCHAR (50),
                        age INTEGER (3),
                        number_of_borrowed_books INTEGER,
                        PRIMARY KEY (id),
                    );"""
    
    borrowed_users = f"""
                    CREATE TABLE {tables[2]}
                    (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        book_id INTEGER,
                        borrow_date VARCHAR (19),
                        return_date VARCHAR (19),
                        returned INTEGER (1),
                        penalty INTEGER,
                        FOREIGN KEY (user_id) REFERENCES {tables[1]}(id),
                        FOREIGN KEY (book_id) REFERENCES {tables[0]}(id)
                    )
                    """
    
    history_of_borrows = f"""
                    CREATE TABLE {tables[3]}
                    (
                        user_id INTEGER,
                        book_id INTEGER,
                        borrowed_day INTEGER,
                        returned_day INTEGER,
                        penalty INTEGER,
                        FOREIGN KEY (user_id) REFERENCES Users(id),
                        FOREIGN KEY (book_id) REFERENCES Books(id),
                        FOREIGN KEY (borrowed_day) REFERENCES BookBorrowedUsers()
                    );"""

    table_names = []
    for table_name in table_names:
        cursor.execute(table_name)

application = QApplication([])

# MAIN WINDOW

application.exec()

cursor.close()
db_connection.close()










# b d e f g i g m a