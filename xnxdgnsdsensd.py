#-*- coding: utf-8 -*-


import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import *


class Game(QMainWindow):
    def __init__(self):
        self.turn = False
        super().__init__()
        uic.loadUi('untitled1.ui', self)
        self.matches = 37
        self.check = True
        self.lb.setText(self.lb.text() + str(self.matches))
        self.btn.clicked.connect(self.take)

    def take(self):
        if int(self.ln.text()) not in [i for i in range(1, 6)]:
            self.lb2.setText('Введено неправильное значение')
            self.lb2.resize(self.lb2.sizeHint())
        else:
            self.lb2.setText('')
            self.matches -= int(self.ln.text())
            if self.matches == 0:
                self.lb1.setText('Победили вы')
                self.btn.setEnabled(False)
                self.check = False
            if self.check:
                self.turn = True
                if self.turn:
                    if self.matches > 11:
                        self.matches -= random.choice([i for i in range(1, 6)])
                    elif self.matches <= 11 and self.matches > 6:
                        if self.matches == 11:
                            self.matches -= 5
                        elif self.matches == 10:
                            self.matches -= 4
                        elif self.matches == 9:
                            self.matches -= 3
                        elif self.matches == 8:
                            self.matches -= 2
                        elif self.matches == 7:
                            self.matches -= 1
                    elif self.matches == 6:
                        self.matches -= 1
                    elif self.matches <= 5:
                        self.matches -= self.matches
                    self.turn = False
                if self.matches == 0:
                    self.lb1.setText('Победил компьютер')
                    self.btn.setEnabled(False)
        self.lb.setText(self.lb.text()[:-2] + str(self.matches).rjust(2, ' '))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = Game()
    mc.show()
    sys.exit(app.exec())
