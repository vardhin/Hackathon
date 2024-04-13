from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QGraphicsBlurEffect, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

def create_page():
    page = QWidget()
    layout = QVBoxLayout()
    label = QLabel("This is Page 1")
    button = QPushButton("Button on Page 1")
    layout.addWidget(label)
    layout.addWidget(button)
    page.setLayout(layout)
    return page
