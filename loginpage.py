import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLineEdit, QWidget, QSizePolicy, QPushButton
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Standardized Education System: SES")
        self.central_widget = QWidget()  # Central widget to hold layout
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)  # Grid layout
        self.create_fields()
        self.create_submit_button()

        # Start timer to update font size per frame
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_font_size)
        self.timer.start(16)  # Update approximately every 16 milliseconds (close to 60 frames per second)

    def create_fields(self):
        # Creating username and password fields
        self.username_field = QLineEdit()
        self.username_field.setPlaceholderText("Username")
        self.password_field = QLineEdit()
        self.password_field.setPlaceholderText("Password")
        self.password_field.setEchoMode(QLineEdit.Password)

        # Setting fields to expand horizontally
        self.username_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.password_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Adding fields to layout
        self.layout.addWidget(self.username_field, 1, 1)  # Row 1, Column 1
        self.layout.addWidget(self.password_field, 2, 1)  # Row 2, Column 1

        # Set row and column stretch
        self.layout.setColumnStretch(0, 1)  # Stretch column 0
        self.layout.setColumnStretch(3, 1)  # Stretch column 3
        self.layout.setRowStretch(0, 1)  # Stretch row 0
        self.layout.setRowStretch(3, 1)  # Stretch row 3

    def create_submit_button(self):
        # Creating submit button
        self.submit_button = QPushButton("Submit")

        # Connecting button click event to submit function
        self.submit_button.clicked.connect(self.submit_form)

        # Adding button to layout
        self.layout.addWidget(self.submit_button, 3, 1)  # Row 3, Column 1

    def update_font_size(self):
        # Dynamically adjust font size based on field size ratio
        font = self.username_field.font()
        font_size = min(self.username_field.size().width(), self.username_field.size().height()) // 15
        font.setPointSize(font_size)
        self.username_field.setFont(font)
        self.password_field.setFont(font)

    def submit_form(self):
        # Fetch entered username and password
        username = self.username_field.text()
        password = self.password_field.text()
        # Do something with the submitted data, like sending it to a server or performing authentication
        print("Username:", username)
        print("Password:", password)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
