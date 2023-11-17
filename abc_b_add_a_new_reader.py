from PyQt5.QtWidgets import (
                            QLabel, QMainWindow, QPushButton,
                            QWidget, QVBoxLayout, QHBoxLayout,
                            QLineEdit, QFileDialog
                            )
# from PyQt5.QtGui import (QPixmap, QPainter, QBitmap, QFont)
from PyQt5.QtCore import Qt, QTimer
import shutil
import os

class NotificationBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__label = QLabel(self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.__label)
        self.setLayout(self.layout)
        self.setFixedHeight(60)
        self.hide()

        self.__timer = QTimer(self)
        self.__timer.timeout.connect(self.__hide_notification)

    def show_notification(self, message, color):
        self.setStyleSheet(f"background-color: {color}; color: white; padding: 8px;")
        self.__label.setText(message)
        self.show()
        self.__timer.start(5000)

    def __hide_notification(self):
        self.hide()
        self.__timer.stop()

class AddNewReader(QMainWindow):
    def __init__(self, first_window, db_connection, cursor, font):
        super().__init__()
        self.__cursor = cursor
        self.__db_connection = db_connection

        self.__user_information = [None] * 6

        self.__font = font

        self.setStyleSheet("QWidget#MyWindow { background-image: url('C:/Users/Gulzhaev/Desktop/library_management/pictures/library_management_wallpaper.jpg'); background-repeat: no-repeat; background-position: center; }")
        self.setObjectName("MyWindow")
        self.__first_window = first_window
        self.setWindowTitle("Add a new reader")

        self.__go_back_button = QPushButton("←")
        self.__go_back_button.clicked.connect(self.__go_back_button_clicked)
        self.__go_back_button.setStyleSheet("QPushButton { color: white; background-color: rgba(171, 171, 171, 0.38)} ")

        self.__text = "enter here"

        self.__main_label = QLabel("<html><b><font size='10'>ENTER USER INFORMATiON</font></b></html>")
        self.__main_label.setStyleSheet("color: rgb(120, 120, 120);")

        self.__go_back_button.setFixedWidth(40)

        self.__passport_serial_requirer_label = QLabel("<html><b><font size='10'>ENTER THE PASSPORT SERIAL</font></b></html>")
        self.__passport_serial_requirer_label.setStyleSheet("color: rgb(120, 120, 120);")

        self.__passport_serial_requirer_line_edit = QLineEdit()
        self.__passport_serial_requirer_line_edit.setStyleSheet("QLineEdit { color: white; background-color: rgba(207, 206, 203, 0.439) };")
        self.__passport_serial_requirer_line_edit.setFixedHeight(30)
        self.__passport_serial_requirer_line_edit.setPlaceholderText(self.__text)
        self.__passport_serial_requirer_line_edit.setFixedWidth(300)

        self.__layout_1 = QHBoxLayout()
        self.__layout_1.addWidget(self.__passport_serial_requirer_label)
        self.__layout_1.addWidget(self.__passport_serial_requirer_line_edit)
        self.__widget_1 = QWidget()
        self.__widget_1.setLayout(self.__layout_1)

        self.__passport_serial_number_requirer_label = QLabel("<html><b><font size='10'>ENTER THE PASSPORT SERIAL NUMBER </font></b></html>")
        self.__passport_serial_number_requirer_label.setStyleSheet("color: rgb(120, 120, 120);")

        self.__passport_serial_number_requirer_line_edit = QLineEdit()
        self.__passport_serial_number_requirer_line_edit.setStyleSheet("QLineEdit { color: white; background-color: rgba(207, 206, 203, 0.439) };")
        self.__passport_serial_number_requirer_line_edit.setFixedHeight(30)
        self.__passport_serial_number_requirer_line_edit.setFixedWidth(300)
        self.__passport_serial_number_requirer_line_edit.setPlaceholderText(self.__text)
        self.__passport_serial_number_requirer_line_edit.returnPressed.connect(
                                        self.__passport_serial_values
        )

        self.__layout_2 = QHBoxLayout()
        self.__layout_2.addWidget(self.__passport_serial_number_requirer_label)
        self.__layout_2.addWidget(self.__passport_serial_number_requirer_line_edit)
        self.__widget_2 = QWidget()
        self.__widget_2.setLayout(self.__layout_2)

        self.__fullname_requirer_label = QLabel("<html><b><font size='10'>ENTER FULLNAME OF USER</font></b></html>")
        self.__fullname_requirer_label.setStyleSheet("color: rgb(171, 171, 171);")

        self.__fullname_requirer_line_edit = QLineEdit()
        self.__fullname_requirer_line_edit.returnPressed.connect(self.__full_name_requirer_label)
        self.__fullname_requirer_line_edit.setStyleSheet("QLineEdit { color: white; background-color: rgba(207, 206, 203, 0.439) };")
        self.__fullname_requirer_line_edit.setFixedHeight(30)
        self.__fullname_requirer_line_edit.setFixedWidth(300)
        self.__fullname_requirer_line_edit.setPlaceholderText(self.__text)

        self.__layout_3 = QHBoxLayout()
        self.__layout_3.addWidget(self.__fullname_requirer_label)
        self.__layout_3.addWidget(self.__fullname_requirer_line_edit)
        self.__widget_3 = QWidget()
        self.__widget_3.setLayout(self.__layout_3)

        self.__age_requirer_label = QLabel("<html><b><font size='10'>ENTER AGE OF USER</font></b></html>")
        self.__age_requirer_label.setStyleSheet("color: white;")

        self.__age_requirer_line_edit = QLineEdit()
        self.__age_requirer_line_edit.setFixedHeight(30)
        self.__age_requirer_line_edit.returnPressed.connect(self.__age_requirer_widget_is_used)
        self.__age_requirer_line_edit.setFixedWidth(300)
        self.__age_requirer_line_edit.setStyleSheet("QLineEdit { color: white; background-color: rgba(207, 206, 203, 0.439) };")
        self.__age_requirer_line_edit.setPlaceholderText(self.__text)

        self.__layout_4 = QHBoxLayout()
        self.__layout_4.addWidget(self.__age_requirer_label)
        self.__layout_4.addWidget(self.__age_requirer_line_edit)
        self.__widget_4 = QWidget()
        self.__widget_4.setLayout(self.__layout_4)

        self.__notification_bar = NotificationBar(self)
        self.__notification_bar.setFixedHeight(40)

        self.__set_user_picture_button = QPushButton("SELECT A USER PiCTURE")
        self.__set_user_picture_button.setFixedHeight(80)
        self.__set_user_picture_button.setStyleSheet("QPushButton { color: white; background-color: rgba(61, 61, 61, 0.471); border: 2px solid rgba(209, 209, 209, 0.459) }"
        "QPushButton:hover { background-color: rgba(207, 206, 203, 0.451) }"
        )
        self.__set_user_picture_button.setFont(self.__font)
        self.__set_user_picture_button.clicked.connect(self.__upload_image_button_clicked)
        aaa = QLabel()
        self.__central_layout = self.__layout_maker(
                            True,
                            self.__main_label,
                            self.__widget_1,
                            self.__widget_2,
                            self.__widget_3,
                            self.__widget_4,
                            self.__set_user_picture_button
        )
        self.__central_layout.setAlignment(self.__main_label, Qt.AlignCenter)
        self.__central_widget = QWidget()
        self.__central_widget.setLayout(self.__central_layout)
        self.__central_widget.setStyleSheet("QWidget#MyBorder { border: 2px solid gray; padding: 10px; }")
        self.__central_widget.setObjectName("MyBorder")
        self.__central_widget.setFixedSize(1100, 700)

        self.__apply_all_button = QPushButton("SUBMiT")
        self.__apply_all_button.clicked.connect(self.__submit_button_clicked)
        self.__apply_all_button.setFixedSize(900, 80)
        self.__apply_all_button.setFont(self.__font)
        self.__apply_all_button.setStyleSheet("QPushButton { color: white; background-color: rgba(61, 61, 61, 0.471) }"
        "QPushButton:hover { background-color: rgba(207, 206, 203, 0.451) }")

        self.__main_layout = self.__layout_maker(
            True,
            self.__go_back_button,
            self.__notification_bar,
            aaa,
            self.__central_widget,
            self.__apply_all_button
        )
        self.__main_layout.setAlignment(self.__apply_all_button, Qt.AlignCenter)
        self.__main_layout.setAlignment(self.__central_widget, Qt.AlignCenter)

        self.__main_widget = QWidget()
        self.__main_widget.setLayout(self.__main_layout)

        self.setCentralWidget(self.__main_widget)

    def __layout_maker(self, is_vertical, * widgets):
        if is_vertical:
            layout = QVBoxLayout()
        else:
            layout = QHBoxLayout()
        for widget in widgets:
            layout.addWidget(widget)
        return layout

    def __go_back_button_clicked(self):
        self.__first_window.resize(self.width(), self.height())
        self.__first_window.move(self.pos())
        self.hide()
        self.__first_window.show()

    def __full_name_requirer_label(self):
        full_name = self.__fullname_requirer_line_edit.text()
        if len(full_name):
            full_name = full_name.upper()
            self.__user_information[2] = full_name

    def __age_requirer_widget_is_used(self):
        text_of_widget = self.__age_requirer_line_edit.text()
        if len(text_of_widget):
            try:
                text_of_widget = int(text_of_widget)
                self.__user_information[3] = text_of_widget
            except:
                self.__notification_bar.show_notification("enter a valid age please", 'red')

    def __consisted_of_english_letters(self, text: str):
        return all(char.isalpha() and ord(char) < 128 for char in text)
    
    def __upload_image_button_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)", options=options)

        if file_name:
            target_directory = "C:/Users/Gulzhaev/Desktop/library_management/pictures"
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)

            _, file_name_only = os.path.split(file_name)

            destination_path = os.path.join(target_directory, file_name_only)
            resulting_destination_path = ''
            for i in destination_path:
                if i == chr(92):
                    resulting_destination_path += '/'
                else:
                    resulting_destination_path += i

            shutil.copy(file_name, resulting_destination_path)
            self.__user_information[5] = resulting_destination_path

    def __passport_serial_values(self):
        passport_serial = self.__passport_serial_requirer_line_edit.text()
        passport_serial_number = self.__passport_serial_number_requirer_line_edit.text()
        if len(passport_serial) == 2 and self.__consisted_of_english_letters(passport_serial):
            query = "SELECT 1 FROM USERS WHERE EXISTS (SELECT 1 FROM USERS WHERE passport_serial = %s AND passport_serial_number = %s)"
            self.__cursor.execute(query, (passport_serial, passport_serial_number))
            result = self.__cursor.fetchone()
            if result:
                self.__notification_bar.show_notification("Something went wrong", 'red')
            else:
                self.__user_information[0] = passport_serial.upper()
                self.__user_information[1] = passport_serial_number
        else:
            self.__notification_bar.show_notification("Please enter a valid passport serial", 'red')

    def __submit_button_clicked(self):
        self.__full_name_requirer_label()
        self.__age_requirer_widget_is_used()
        self.__passport_serial_values()
        counter = 0
        for i in self.__user_information:
            if i is None:
                counter += 1
        if counter == 1:
            try:
                query = """INSERT INTO Users (passport_serial, passport_serial_number, full_name, age, number_of_borrowed_books, path_to_user_s_pic)
                            VALUES (%s, %s, %s, %s, %s, %s)"""
                self.__cursor.execute(query, tuple(self.__user_information))
                self.__db_connection.commit()
                self.__notification_bar.show_notification("User has been added successfully", 'green')
                self.__clear_input_fields()
            except Exception as e:
                self.__notification_bar.show_notification("Something went wrong. Please try again.", 'red')
        else:
            self.__notification_bar.show_notification("Please fill all the requirements", 'red')

    def __clear_input_fields(self):
        self.__passport_serial_requirer_line_edit.clear()
        self.__passport_serial_number_requirer_line_edit.clear()
        self.__fullname_requirer_line_edit.clear()
        self.__age_requirer_line_edit.clear()
