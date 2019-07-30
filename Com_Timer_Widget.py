import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ComputerTimePrint(QWidget):

    def __init__(self):
        super().__init__()
        self.init_quit_time()
        self.initUI()


    def initUI(self):

        lbl = QLabel('종료 시간')

        self.timeedit = QTimeEdit(self)
        self.timeedit.setTime(QTime(int(self.quit_time[0]), int(self.quit_time[1])))
        self.timeedit.setDisplayFormat('hh:mm')

        self.save_btn = QPushButton('저장', self)
        self.save_btn.clicked.connect(self.save_btn_clicked)

        hbox1 = QHBoxLayout()
        hbox1.addStretch()
        hbox1.addWidget(lbl)
        hbox1.addStretch()

        hbox2 = QHBoxLayout()
        hbox2.addStretch()
        hbox2.addWidget(self.timeedit)
        hbox2.addStretch()

        hbox3 = QHBoxLayout()
        hbox3.addStretch()
        hbox3.addWidget(self.save_btn)
        hbox3.addStretch()


        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.setAlignment(Qt.AlignVCenter)

        self.setLayout(vbox)


    def init_quit_time(self):

        f = open("Computer_time.txt", 'r')
        temp = f.read()
        temp2 = temp.split(':')
        self.quit_time = temp2
        print(self.quit_time)
        f.close()


    def save_btn_clicked(self):

        temp = self.timeedit.text()
        with open('Computer_time.txt', 'w', encoding='UTF8') as fp:
            fp.write(temp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ComputerTimePrint()
    sys.exit(app.exec_())