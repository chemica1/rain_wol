import os, sys, threading
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from Com_Controll_Widget import ComputerListPrint
from Com_Info_Widget import ComputerInfoPrint
from Com_Timer_Widget import ComputerTimePrint
from Loading_Widget import Loding_Widget
from wakeonlan import send_magic_packet
from Remote_Off import Remote_off_class
from datetime import timedelta

class MainWindow(QMainWindow): #메인윈도우에선 layout 못쓴다. 자체레이아웃을 갖고있기때문

    def __init__(self):

        super().__init__()
        self.dir_path = os.getcwd()
        self.list_of_start_time = []
        self.list_of_name = []
        self.list_of_IP = []
        self.list_of_MAC = []
        self.file_to_list()
        self.init_quit_time()
        self.quit_flag = 0
        self.quit_temp = Remote_off_class('123')

        self.initTimer()
        self.initPowerOn()
        self.initUI()
        QTimer.singleShot(3000, self.showComputerList)


    def initUI(self):

        self.setWindowTitle('WOL for huliac')
        self.setWindowIcon(QIcon(f'{self.dir_path}\\huliacLogo.png'))

        list_toolbar = QAction(QIcon(f'{self.dir_path}\\poweron.png'), '전원제어', self)
        list_toolbar.setStatusTip('컴퓨터를 제어합니다.')
        list_toolbar.triggered.connect(self.showComputerList)
        self.toolbar = self.addToolBar('list_toolbar')
        self.toolbar.addAction(list_toolbar)

        info_toolbar = QAction(QIcon(f'{self.dir_path}\\edit.png'), '정보변경', self)
        info_toolbar.setStatusTip('컴퓨터 정보를 변경합니다.')
        info_toolbar.triggered.connect(self.showComputerInfo)
        self.toolbar = self.addToolBar('info_toolbar')
        self.toolbar.addAction(info_toolbar)

        time_toolbar = QAction(QIcon(f'{self.dir_path}\\time.png'), '스케줄설정', self)
        time_toolbar.setStatusTip('종료 시간을 설정합니다.')
        time_toolbar.triggered.connect(self.showComputerTime)
        self.toolbar = self.addToolBar('time_toolbar')
        self.toolbar.addAction(time_toolbar)

        question_toolbar = QAction(QIcon(f'{self.dir_path}\\question.png'), '문의사항', self)
        question_toolbar.setStatusTip('종료 시간을 설정합니다.')
        #info_toolbar.triggered.connect(self.showComputerInfo)
        self.toolbar = self.addToolBar('question_toolbar')
        self.toolbar.addAction(question_toolbar)

        info_toolbar.setEnabled(False)
        list_toolbar.setEnabled(False)
        time_toolbar.setEnabled(False)
        question_toolbar.setEnabled(False)

        self.showLoadingMovie()
        QTimer.singleShot(1500, self.showLoadingMovie2)
        QTimer.singleShot(3000, lambda: info_toolbar.setEnabled(True))
        QTimer.singleShot(3000, lambda: list_toolbar.setEnabled(True))
        QTimer.singleShot(3000, lambda: time_toolbar.setEnabled(True))
        QTimer.singleShot(3000, lambda: question_toolbar.setEnabled(True))

        self.statusBar()

        self.setGeometry(100, 100, 800, 400)
        self.show()


    def initPowerOn(self):

        print(f'현재시각 {QTime.currentTime().toString()}')
        current_time = QTime.currentTime().toString().split(':')
        for i in range(0,10):
            start_time_temp = self.list_of_start_time[i].split(':')  #설정된 시간을 리스트로 뽑아낸다. 시 / 분 / 초
            start_td = timedelta(hours=int(start_time_temp[0]), minutes=int(start_time_temp[1]), seconds=int(start_time_temp[2]))
            current_td = timedelta(hours=int(current_time[0]), minutes=int(current_time[1]), seconds=int(current_time[2]))
            remaining_td = start_td - current_td  #설정된 시간과 현재시간간의 시간차를 구한다.

            QTimer.singleShot(int(remaining_td.seconds), lambda : send_magic_packet(self.list_of_MAC[i])) # 몇초후에 매직패킷을 보낼건지.
            print(f'{remaining_td.seconds}초 후에 {(i+1)}번 컴퓨터({self.list_of_MAC[i]})를 킵니다.')


    def init_quit_time(self):

        f = open(f'{self.dir_path}\\Computer_time.txt', 'r')
        temp = f.read()
        temp2 = temp.split(':')
        self.quit_time = temp2
        f.close()


    def initTimer(self):

        self.timer = QTimer()
        self.timer.timeout.connect(self.MainTimer)
        self.timer.start(1000)


    def MainTimer(self): # 매초마다 연산하는 타이머.. 어떤 시간종속적인 일을 하고싶다면 여기에 넣으면 된다.

        date = QDate.currentDate()
        time = QTime.currentTime().toString()
        time_temp = time.split(':')

        remaining_hour = int(self.quit_time[0]) - int(time_temp[0])
        remaining_minute = int(self.quit_time[1]) - int(time_temp[1])

        if remaining_hour == 0 and remaining_minute == 0 and self.quit_flag == 0:
            self.quit_flag = 1
            QTimer.singleShot(200, lambda : self.turn_off_computer_start())

        if self.quit_flag == 0:
            self.statusBar().showMessage(date.toString(Qt.DefaultLocaleLongDate) + ' ' + time + f'  종료 예약 : {self.quit_time[0]}시 {self.quit_time[1]}분') #시간표시
        else:
            self.statusBar().showMessage('모든 컴퓨터를 종료한 뒤 프로그램이 자동으로 꺼집니다. 전원을 끄지 말아주세요.')
            QTimer.singleShot(100000, lambda : sys.exit())


    def turn_off_computer_start(self):

        threads = []
        for IP in self.list_of_IP:
            t = threading.Thread(target=self.turn_off_computer_method,
                                 args=(IP,))  # 쓰레딩 할때... iterable형으로 args를 넣어야하는걸 잊지마라. 즉 쉼표 붙여주란소리임.
            threads.append(t)
        ##각각의 쓰레드를 시작하고 및 끝날때까지 기다림(조인)
        for t in threads:
            t.start()
        for t in threads:
            t.join()


    def turn_off_computer_method(self, IP):
        self.quit_temp.power_off_etc(IP)
        print(IP + '를 종료했습니다!!!')


    def initWindowWhere(self): #처음 켜지는 창 윈도우에서의 위치 정하는 함수. 일단 정중앙으로 위치하게 만든거임.

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


    def showComputerTime(self):

        ComputerTimeWidget = ComputerTimePrint()
        self.setCentralWidget(ComputerTimeWidget)


    def file_to_list(self):

        # IP 리스트
        file = open(f'{self.dir_path}\\Computer_IP.txt', 'r', encoding='UTF8')
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
        file = open(f'{self.dir_path}\\Computer_MAC.txt', 'r', encoding='UTF8')
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

        # start_time 리스트
        file = open(f'{self.dir_path}\\Computer_start_time.txt', 'r', encoding='UTF8')
        while (1):
            line = file.readline()
            try:
                escape = line.index('\n')
            except:
                escape = len(line)
            if line:
                self.list_of_start_time.append(line[0:escape])
            else:
                break
        file.close()

        # 컴퓨터 이름 리스트
        file = open(f'{self.dir_path}\\Computer_name.txt', 'r', encoding='UTF8')
        while (1):
            line = file.readline()
            try:
                escape = line.index('\n')
            except:
                escape = len(line)
            if line:
                self.list_of_name.append(line[0:escape])
            else:
                break
        file.close()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())