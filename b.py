from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import choice
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(500, 500)
        self.btn = QPushButton('Круги', self)
        self.btn.resize(101, 23)
        self.btn.move(200, 460)
        self.btn.clicked.connect(self.button)

    def button(self):
        self.update()

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.circles(qp)
        qp.end()

    def circles(self, qp):
        for i in range(10):
            qp.setBrush(QColor(choice(range(255)), choice(range(255)), choice(range(255))))
            size = choice(range(300))
            qp.drawEllipse(choice(range(300)), choice(range(300)),
                           size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())