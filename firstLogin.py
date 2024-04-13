import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt

class BackgroundWidget(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path
        self.pixmap = QPixmap(self.image_path)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Screen Changer')
        self.setGeometry(100, 100, 400, 300)

        self.background = BackgroundWidget("pic.jpg")
        self.label = QLabel("Main Screen")
        self.label.setAlignment(Qt.AlignCenter)

        self.button1 = QPushButton('Go to Screen 1')
        self.button1.clicked.connect(self.screen1)

        self.button2 = QPushButton('Go to Screen 2')
        self.button2.clicked.connect(self.screen2)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(self.background)
        central_layout.addLayout(layout)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)  # Set the central widget of the main window

    def screen1(self):
        self.label.setText("You're on Screen 1")
        self.button1.hide()
        self.button2.show()

    def screen2(self):
        self.label.setText("Welcome to Screen 2")
        self.button2.hide()
        self.button1.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWidget()
    main_window.show()
    sys.exit(app.exec_())
