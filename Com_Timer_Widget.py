import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ComputerTimePrint(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lbl = QLabel('QTimeEdit')

        timeedit = QTimeEdit(self)
        timeedit.setTime(QTime.currentTime())
        timeedit.setDisplayFormat('hh:mm')

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(timeedit)
        vbox.setAlignment(Qt.AlignVCenter)

        self.setLayout(vbox)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ComputerTimePrint()
    sys.exit(app.exec_())