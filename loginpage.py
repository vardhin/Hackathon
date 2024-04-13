from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QGraphicsBlurEffect, QWidget, QSpacerItem, QSizePolicy, QLineEdit
from PyQt5.QtGui import QPixmap, QImage, QPalette, QPainter, QFont, QColor, QBrush
from PyQt5.QtCore import Qt, QSize

def create_login_page():
    page = QWidget()

    # Set background image
    background_image = QImage("pic.jpg")
    palette = QPalette()
    brush = QBrush(background_image)
    palette.setBrush(QPalette.Background, brush)
    page.setAutoFillBackground(True)
    page.setPalette(palette)

    layout = QVBoxLayout()

    # Username Label and Input
    username_label = QLabel("Username:")
    username_label.setStyleSheet("color: white; font-size: 20px;")
    layout.addWidget(username_label)
    username_input = QLineEdit()
    username_input.setStyleSheet("background-color: rgba(255, 255, 255, 0.3); color: white; font-size: 16px; border-radius: 5px; padding: 10px;")
    layout.addWidget(username_input)

    # Password Label and Input
    password_label = QLabel("Password:")
    password_label.setStyleSheet("color: white; font-size: 20px;")
    layout.addWidget(password_label)
    password_input = QLineEdit()
    password_input.setEchoMode(QLineEdit.Password)
    password_input.setStyleSheet("background-color: rgba(255, 255, 255, 0.3); color: white; font-size: 16px; border-radius: 5px; padding: 10px;")
    layout.addWidget(password_input)

    # Spacer
    layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    # Login Button
    login_button = QPushButton("Login")
    login_button.setStyleSheet("color: white; background-color: #007bff; border: none; padding: 15px 30px; border-radius: 10px; font-size: 18px;")
    layout.addWidget(login_button)
    layout.setAlignment(login_button, Qt.AlignCenter)

    # Set layout margins
    layout.setContentsMargins(100, 200, 100, 200)

    page.setLayout(layout)

    return page
