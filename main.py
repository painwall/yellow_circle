import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.btn_draw.clicked.connect(self.edit_flag)

    def edit_flag(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.flag = False
            qp = QPainter()
            qp.begin(self)
            self.drawFlag(qp)
            qp.end()

    def drawFlag(self, qp):
        r = randint(10, 150)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(150, 150, 150 + r, 150 + r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
