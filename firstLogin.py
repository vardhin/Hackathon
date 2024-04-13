import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QGraphicsBlurEffect, QGridLayout, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt

class BackgroundWidget(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path
        self.pixmap = QPixmap(self.image_path)
        
        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(10)  # Set the blur radius (adjust as needed)

        self.background_label = QLabel(self)
        self.background_label.setPixmap(self.pixmap)
        self.background_label.setScaledContents(True)

        self.background_label.setGraphicsEffect(self.blur_effect)

    def resizeEvent(self, event):
        self.background_label.setGeometry(0, 0, self.width(), self.height())

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Screen Changer')
        self.setGeometry(100, 100, 500, 800)

        self.background = BackgroundWidget("pic.jpg")
        self.setCentralWidget(self.background)  # Set background as central widget

        self.label = QLabel("Main Screen")
        self.label.setAlignment(Qt.AlignCenter)

        self.grid_layout = QVBoxLayout()

        self.button1 = QPushButton('Go to Screen 1')
        self.button1.clicked.connect(self.screen1)

        self.button2 = QPushButton('Go to Screen 2')
        self.button2.clicked.connect(self.screen2)

        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.grid_layout.addWidget(self.label)
        self.grid_layout.addItem(spacer_item)
        self.grid_layout.addWidget(self.button1, alignment=Qt.AlignCenter)
        self.grid_layout.addWidget(self.button2, alignment=Qt.AlignCenter)

        self.background.setLayout(self.grid_layout)  # Add grid layout to the background

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
