import random
import sys

from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPen, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class YellowCirclesWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.status = False
        # self.setupUi(self)
        self.ellipses = [[]]
        self.setWindowTitle("Git и желтые окружности")
        uic.loadUi("UI.ui", self)
        self.generate_circles()

    def generate_circles(self):
        self.pushButton.clicked.connect(self.draw)
        self.show()

    def draw(self):
        self.status = True
        self.ellipses[-1].append(random.randint(15, 75))
        self.ellipses[-1].append(random.randint(0, 500))
        self.ellipses[-1].append(random.randint(0, 480))
        self.ellipses[-1].append(random.randint(1, 10))
        self.ellipses.append([])
        self.repaint()

    def paintEvent(self, event):
        if self.status:
            qp = QPainter()
            qp.begin(self)
            for circle in self.ellipses[:-1]:
                pen = QPen(QColor(random.randint(0, 255), random.randint(0, 255),
                    random.randint(0, 255)))
                pen.setWidth(circle[random.randint(-1, 1)])
                qp.setPen(pen)
                qp.drawEllipse(*circle[:-1], circle[-2])
            qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = YellowCirclesWidget()
    ex.show()
    sys.exit(app.exec_())
