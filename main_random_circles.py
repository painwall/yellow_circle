from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
from random import randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_draw = QtWidgets.QPushButton(self.centralwidget)
        self.btn_draw.setGeometry(QtCore.QRect(690, 580, 111, 23))
        self.btn_draw.setObjectName("btn_draw")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_draw.setText(_translate("MainWindow", "Нарисовать круг"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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

        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(150, 150, 150 + r, 150 + r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
