# lines.py

import math
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

def draw_lines(num_lines, angles, start_x, start_y):
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    
    widget = QWidget()
    widget.setGeometry(100, 100, 300, 300)  # Default size
    widget.setWindowTitle('Drawing Lines')

    length = min(widget.width(), widget.height()) / 2

    def paint_event(event):
        painter = QPainter(widget)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        
        for angle_degrees in angles:
            angle_radians = math.radians(angle_degrees)
            end_x = start_x + length * math.cos(angle_radians)
            end_y = start_y + length * math.sin(angle_radians)
            end_x = round(end_x)
            end_y = round(end_y)
            painter.drawLine(start_x, start_y, end_x, end_y)

    widget.paintEvent = paint_event
    widget.show()
    app.exec_()

# Example usage:
if __name__ == '__main__':
    num_liness = 20
    draw_lines(num_liness, [15 * i for i in range(num_liness)], 150, 150)  # Example parameters
