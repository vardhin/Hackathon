import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QSizePolicy
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Standardized Education System: SES")
        self.central_widget = QWidget()  # Central widget to hold layout
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)  # Vertical layout
        self.create_buttons()

        # Start timer to update font size per frame
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_font_size)
        self.timer.start(16)  # Update approximately every 16 milliseconds (close to 60 frames per second)

    def create_buttons(self):
        # Creating buttons
        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")
        self.button3 = QPushButton("Button 3")

        # Setting buttons to expand horizontally
        self.button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Adding buttons to layout
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)

    def update_font_size(self):
        # Dynamically adjust font size based on button size ratio
        font = self.button1.font()
        font_size = min(self.button1.size().width(), self.button1.size().height()) // 10
        font.setPointSize(font_size)
        self.button1.setFont(font)
        self.button2.setFont(font)
        self.button3.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())