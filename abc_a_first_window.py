from PyQt5.QtWidgets import (
                            QLabel, QMainWindow, QPushButton,
                            QWidget, QVBoxLayout, QHBoxLayout
                            )
from PyQt5.QtGui import (QPixmap, QPainter, QBitmap, QFont)
from PyQt5.QtCore import Qt

class FirstWindow(QMainWindow):
    def __init__(self, library_name: str):
        super().__init__()
        self.setWindowTitle(library_name)
        self.setStyleSheet("QWidget#MyWindow { background-image: url('C:/Users/Gulzhaev/Desktop/library_management/pictures/library_management_wallpaper.jpg'); background-repeat: no-repeat; background-position: center; }")
        self.setObjectName("MyWindow")
        self.resize(1200, 1000)

        self.__image_ofLibrary = QLabel(self)
        self.__pixmap = QPixmap(
            "C:/Users/Gulzhaev/Desktop/library_management/pictures/library_picture.JPG"
            )
        self.__circular_mask = QBitmap(220, 220)
        self.__circular_mask.fill(Qt.white)
        self.__painter = QPainter(self.__circular_mask)
        self.__painter.setRenderHint(QPainter.Antialiasing)
        self.__painter.setBrush(Qt.black)
        self.__painter.drawEllipse(0, 0, 220, 220)
        self.__painter.end()

        font = QFont()
        font.setBold(True)
        font.setPointSize(10)

        self.__scaled_pixmap = self.__pixmap.scaled(220, 220, aspectRatioMode=Qt.KeepAspectRatio)
        self.__image_ofLibrary.setPixmap(self.__scaled_pixmap)
        self.__image_ofLibrary.setMask(self.__circular_mask)

        self.__library_name = QLabel("<html><b><font size='20'>Minnie Muse</font></b></html>")
        self.__library_name.setStyleSheet("color: gray;")
        self.__register_a_user_button = QPushButton("ADD A NEW READER")
        self.__register_a_user_button.setFixedSize(1000, 80)
        self.__register_a_user_button.setStyleSheet("QPushButton { color: white; background-color: rgba(122, 122, 122, 0.451) }"
        "QPushButton:hover { background-color: rgba(207, 206, 203, 0.451) }")
        self.__register_a_user_button.setFont(font)
        
        self.__lend_a_book_button = QPushButton("BOOK LENDiNG")
        self.__lend_a_book_button.setFixedSize(1000, 80)
        self.__lend_a_book_button.setStyleSheet("QPushButton { color: white; background-color: rgba(122, 122, 122, 0.451) }"
        "QPushButton:hover { background-color: rgba(207, 206, 203, 0.451) }")
        self.__lend_a_book_button.setFont(font)
        
        self.__see_book_borrowers_button = QPushButton("REPORTS")
        self.__see_book_borrowers_button.setFixedSize(1000, 80)
        self.__see_book_borrowers_button.setStyleSheet("QPushButton { color: white; background-color: rgba(122, 122, 122, 0.451) }"
        "QPushButton:hover { background-color: rgba(207, 206, 203, 0.451) }")
        self.__see_book_borrowers_button.setFont(font)

        self.__show_all_users_button = QPushButton("SHOW ALL USERS")
        self.__show_all_users_button.setFixedSize(1000, 80)
        self.__show_all_users_button.setStyleSheet("QPushButton { color: white; background-color: rgba(122, 122, 122, 0.451) }"
        "QPushButton:hover { background-color: rgba(207, 206, 203, 0.451) }")
        self.__show_all_users_button.setFont(font)

        self.__main_layout = self.__layout_maker(
                                                True,
                                                self.__image_ofLibrary,
                                                self.__library_name,
                                                self.__register_a_user_button,
                                                self.__lend_a_book_button,
                                                self.__see_book_borrowers_button,
                                                self.__show_all_users_button
                                                )
        self.__main_layout.setAlignment(self.__image_ofLibrary, Qt.AlignCenter)
        self.__main_layout.setAlignment(self.__library_name, Qt.AlignCenter)
        self.__main_layout.setAlignment(self.__register_a_user_button, Qt.AlignCenter)
        self.__main_layout.setAlignment(self.__lend_a_book_button, Qt.AlignCenter)
        self.__main_layout.setAlignment(self.__see_book_borrowers_button, Qt.AlignCenter)
        self.__main_layout.setAlignment(self.__show_all_users_button, Qt.AlignCenter)
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

