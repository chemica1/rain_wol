import sys, threading, time
import subprocess, platform
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from Com_Controll_Widget import ComputerListPrint
from Com_Info_Widget import ComputerInfoPrint
from Loading_Widget import Loding_Widget
from wakeonlan import send_magic_packet


class MainWindow(QMainWindow): #메인윈도우에선 layout 못쓴다. 자체레이아웃을 갖고있기때문

    def __init__(self):
        super().__init__()

        self.list_of_IP = []
        self.list_of_MAC = []
        self.file_to_list()

        self.initTimer()
        self.initPowerOn()
        self.initUI()
        QTimer.singleShot(30000, self.showComputerList)


    def initUI(self):

        self.setWindowTitle('WOL for huliac')
        self.setWindowIcon(QIcon('huliacLogo.png'))

        list_toolbar = QAction(QIcon('poweron.png'), '전원제어', self)
        list_toolbar.setStatusTip('현재 컴퓨터 상태를 조작합니다.')
        list_toolbar.triggered.connect(self.showComputerList)
        self.toolbar = self.addToolBar('list_toolbar')
        self.toolbar.addAction(list_toolbar)

        info_toolbar = QAction(QIcon('edit.png'), '정보변경', self)
        info_toolbar.setStatusTip('컴퓨터 정보를 변경합니다.')
        info_toolbar.triggered.connect(self.showComputerInfo)
        self.toolbar = self.addToolBar('info_toolbar')
        self.toolbar.addAction(info_toolbar)

        info_toolbar.setEnabled(False)
        list_toolbar.setEnabled(False)

        self.showLoadingMovie()
        QTimer.singleShot(15000, self.showLoadingMovie2)
        QTimer.singleShot(30000, lambda: info_toolbar.setEnabled(True))
        QTimer.singleShot(30000, lambda: list_toolbar.setEnabled(True))

        self.statusBar()
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate) + ' '+self.time.toString()) #시간표시

        self.resize(800, 400)
        self.initWindowWhere()
        self.show()


    def initPowerOn(self):
        for i in self.list_of_MAC:
            send_magic_packet(i)
            print(i)


    def initTimer(self):

        self.date = QDate.currentDate()
        self.time = QTime.currentTime()


    def initWindowWhere(self): #처음 켜지는 창 윈도우에서의 위치 정하는 함수

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def showComputerList(self):

        ComputerListWidget = ComputerListPrint()
        self.setCentralWidget(ComputerListWidget) #센터 레이아웃에 꼭 추가해줘야한다.


    def showComputerInfo(self):

        SettingComputer = ComputerInfoPrint()
        self.setCentralWidget(SettingComputer) #센터 레이아웃에 꼭 추가해줘야한다.


    def showLoadingMovie(self):

        loading_widget = Loding_Widget("컴퓨터 전원 키는 중...")
        self.setCentralWidget(loading_widget)  # 센터 레이아웃에 꼭 추가해줘야한다.


    def showLoadingMovie2(self):

        loading_widget = Loding_Widget("핑 테스트중...")
        self.setCentralWidget(loading_widget)  # 센터 레이아웃에 꼭 추가해줘야한다.


    def file_to_list(self):

        # IP 리스트
        file = open('Computer_IP.txt', 'r', encoding='UTF8')
        while (1):
            line = file.readline()
            try:
                escape = line.index('\n')
            except:
                escape = len(line)
            if line:
                self.list_of_IP.append(line[0:escape])
            else:
                break
        file.close()

        # MAC 리스트
        file = open('Computer_MAC.txt', 'r', encoding='UTF8')
        while (1):
            line = file.readline()
            try:
                escape = line.index('\n')
            except:
                escape = len(line)
            if line:
                self.list_of_MAC.append(line[0:escape])
            else:
                break
        file.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())