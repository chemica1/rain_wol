import sys
import os
import subprocess, platform

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime, Qt
from PyQt5.QtWidgets import *
from wakeonlan import send_magic_packet


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        btn1 = QPushButton('1')
        btn2 = QPushButton('2')
        layout = QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)
        btn1.clicked.connect(self.btn1_clicked)

        self.setWindowTitle("QWidget")
        self.show()

    def btn1_clicked(self):
        mess = 'nno'
        tf = self.pingOk('192.168.200.3')
        if tf:
            mess = 'hi'

        QMessageBox.about(self, "message", mess)
        send_magic_packet('F8.32.E4.A4.53.93')


    def check_ping(self):
        hostname = "naver.com"
        response = os.system("ping -c 1 " + hostname)
        # and then check the response...
        if response == 0:
            pingstatus = "Network Active"
        else:
            pingstatus = "Network Error"

        return pingstatus

    def pingOk(self, sHost):
        try:
            output = subprocess.check_output(
                "ping -{} 1 {}".format('n' if platform.system().lower() == "windows" else 'c', sHost), shell=True)

        except Exception as e:
            return False

        return True


class MainWindow(QMainWindow):  #Qmainwindow는 자체 레이아웃을 갖고 잇으므로 widget,qdialog처럼 layout 사용 못함

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.time = QTime.currentTime()
        self.initUI()

    def initUI(self):

        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate) + ' '+self.time.toString()) #시간표시
        self.setWindowTitle('Wake on Lan for Huliac')
        self.setWindowIcon(QIcon('huliacLogo.png'))

        wg = CentralWidget()
        self.setCentralWidget(wg)  # 반드시 필요함.

        self.move(700, 300)
        self.resize(400, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())