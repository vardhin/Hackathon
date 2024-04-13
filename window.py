import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGraphicsBlurEffect, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QStackedLayout

class BackgroundWidget(QWidget):
    def _init_(self, image_path):
        super()._init_()
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


class MyWindow(QMainWindow):
    def _init_(self):
        super()._init_()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('SES')
        self.setGeometry(100, 100, 500, 800)
        
        self.stacked_layout = QStackedLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

    def switch_to_page(self, page):
        index = self.stacked_layout.addWidget(page)
        self.stacked_layout.setCurrentIndex(index)

    def remove_current_page(self):
        if self.stacked_layout.count() > 0:
            self.stacked_layout.removeWidget(self.stacked_layout.currentWidget())


if _name_ == '_main_':
    app = QApplication(sys.argv)
    main_window = MyWindow()
    main_window.show()
    sys.exit(app.exec_())
