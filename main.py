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
    
    tables = ["Books", "Users", "HistoryOfBooksUserBorrowed", "BookBorrowedUsers"]

    products_table = f"""
                        CREATE TABLE {tables[0]}
                        (
                            id INTEGER auto_increment,
                            product_name VARCHAR(30),
                            product_price INTEGER,
                            product_category VARCHAR(30),
                            PRIMARY KEY (id)
                        );"""
                        
    cart_table = f"""
                    CREATE TABLE {tables[1]}
                    (
                        id INTEGER,
                        PRIMARY KEY (id)
                    );"""

    purchase_history_table = f"""
                                CREATE TABLE {tables[2]}
                                (
                                    id INTEGER auto_increment,
                                    cart_id INTEGER,
                                    status INTEGER(1),
                                    PRIMARY KEY (id),
                                    FOREIGN KEY (cart_id) REFERENCES Cart(id)
                                );"""

    users_table = f"""
                    CREATE TABLE {tables[3]}
                    (
                        id INTEGER auto_increment,
                        username VARCHAR(30),
                        cart_id INTEGER,
                        purchase_history_table_id INTEGER,
                        PRIMARY KEY (id),
                        FOREIGN KEY (purchase_history_table_id) REFERENCES purchase_history(id),
                        FOREIGN KEY (cart_id) REFERENCES Cart(id)
                    );"""

    products_for_cart = f"""
                    CREATE TABLE {tables[4]}
                    (
                        cart_id INTEGER,
                        product_id INTEGER,
                        FOREIGN KEY (cart_id) REFERENCES Cart(id) ON DELETE CASCADE,
                        FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE
                    );"""

    table_names = [products_table, cart_table, purchase_history_table, users_table, products_for_cart]
    for table_name in table_names:
        cursor.execute(table_name)

application = QApplication([])

# MAIN WINDOW

application.exec()

cursor.close()
db_connection.close()
