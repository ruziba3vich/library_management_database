from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
import shutil
import os

class ImageUploader(QWidget):
    def __init__(self):
        super().__init__()

        self.image_label = QLabel("Selected Image will be displayed here.")
        self.upload_button = QPushButton("Upload Image")
        self.upload_button.clicked.connect(self.upload_image)

        layout = QVBoxLayout(self)
        layout.addWidget(self.image_label)
        layout.addWidget(self.upload_button)

    def upload_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)", options=options)

        if file_name:
            # Display the selected image
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

            # Save the selected image to a specified directory
            target_directory = "C:/Users/Gulzhaev/Desktop/library_management/pictures"
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)

            # Extract the file name from the full path
            _, file_name_only = os.path.split(file_name)

            # Construct the destination path
            destination_path = os.path.join(target_directory, file_name_only)

            # Copy the file to the destination directory
            shutil.copy(file_name, destination_path)
            print(f"Image saved to: {destination_path}")

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = ImageUploader()
    window.show()
    sys.exit(app.exec_())

# "C:/Users/Gulzhaev/Desktop/library_management/pictures"







# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
# from PyQt5.QtCore import QTimer

# class NotificationBar(QWidget):
#     def __init__(self, color, parent=None):
#         super().__init__(parent)
#         self.label = QLabel(self)
#         self.layout = QVBoxLayout(self)
#         self.layout.addWidget(self.label)
#         self.setLayout(self.layout)
#         self.setStyleSheet(f"background-color: {color}; color: white; padding: 8px;")
#         self.setFixedHeight(40)
#         self.hide()

#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.hide_notification)

#     def show_notification(self, message):
#         self.label.setText(message)
#         self.show()
#         self.timer.start(5000)  # Set the duration in milliseconds (5 seconds in this example)

#     def hide_notification(self):
#         self.hide()
#         self.timer.stop()

# class YourMainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Your GUI setup here

#         self.notification_bar = NotificationBar(self)
#         self.setCentralWidget(self.notification_bar)

#         # Example button to trigger a notification
#         self.button = QPushButton("Show Notification", self)
#         self.button.clicked.connect(self.show_example_notification)

#     def show_example_notification(self):
#         self.notification_bar.show_notification("This is a sample notification.")

# # Instantiate and run your application
# app = QApplication([])
# main_window = YourMainWindow()
# main_window.show()
# app.exec_()
