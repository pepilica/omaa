import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 500, 500)

        self.btn = QPushButton('Расчитать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(225, 125)
        self.btn.clicked.connect(self.Count)

        self.ln1 = QLineEdit(self)
        self.ln1.move(100, 100)
        self.ln2 = QLineEdit(self)
        self.ln2.move(300, 100)

        self.sum = QLCDNumber(self)
        self.sum.move(100, 400)
        self.dif = QLCDNumber(self)
        self.dif.move(200, 400)
        self.div = QLCDNumber(self)
        self.div.move(300, 400)
        self.mul = QLCDNumber(self)
        self.mul.move(400, 400)

    def Count(self):
        self.sum.display(int(self.ln1.text()) + int(self.ln2.text()))
        self.dif.display(int(self.ln1.text()) - int(self.ln2.text()))
        if int(self.ln2.text()) != 0:
            self.div.display(int(self.ln1.text()) / int(self.ln2.text()))
        else:
            self.div.display('error')
        self.mul.display(int(self.ln1.text()) * int(self.ln2.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cal = Calculator()
    cal.show()
    sys.exit(app.exec())
