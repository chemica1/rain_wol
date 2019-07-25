from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from magic_packet import send_packet_class
import sys, threading, subprocess, platform


class ComputerListPrint(QWidget):

    def __del__(self):
        print("1가 없어졌어요!")
        self.timer.stop()


    def __init__(self):

        super().__init__()

        self.list_of_name = []
        self.list_of_IP = []
        self.list_of_MAC = []
        self.list_of_packetClass = []
        self.file_to_list()

        self.computer_name = []  #원소가 없는 상태에서 = 연산자로 대입 불가능함. append나 insert 둘 중 하나로 해야됨.
        self.computer_status = []
        self.computer_btn = []

        self.initUI()
        QTimer.singleShot(1000, self.initPingTest)
        self.initBtn()
        self.initTimer()


    def initUI(self):

        self.whole_box = QGroupBox('컴퓨터 제어')

        self.all_button = QPushButton('All Power On', self) #뒤에 self는 속할 부모클래스를 지정해줌
        self.all_button.setStyleSheet("background-color: gray; border-style: outset; border-width: 2px; border-radius: 10px; border-color: gray; font: bold 14px;  padding: 6px; color : white; ")
        self.all_button.clicked.connect(self.All_btn_clicked)

        self.whole_layout = QHBoxLayout()
        self.whole_layout.addStretch(1)
        self.whole_layout.addWidget(self.all_button)
        self.whole_layout.addStretch(1)
        self.whole_box.setLayout(self.whole_layout)

        self.power_box = QGroupBox('개별 제어 & 모니터링')

        for i in range(0, 10):
            self.computer_name.insert(i, QLabel(self.list_of_name[i], self))
            self.computer_name[i].setStyleSheet("bold 11px; ")
            self.computer_status.insert(i, QLabel())
            self.computer_btn.insert(i, QPushButton('Power on', self))


        self.computer_layout = QGridLayout()
        for i in range(0, 10):
            self.computer_layout.addWidget(self.computer_name[i], i, 0)
            self.computer_layout.addWidget(self.computer_status[i], i, 1)
            self.computer_layout.addWidget(self.computer_btn[i], i, 2)
        self.power_box.setLayout(self.computer_layout)

        self.layout = QGridLayout()
        self.layout.addWidget(self.whole_box, 0, 0)
        self.layout.addWidget(self.power_box, 1, 0)
        self.setLayout(self.layout)


    def All_btn_clicked(self):
        for i in range (0,10):
            self.list_of_packetClass[i].send_packet()

    def onActivated(self, text):

        self.Label_Combo.setText(text)
        self.Label_Combo.adjustSize()


    def onChanged(self, text):

        self.Label_Test.setText(text)
        self.Label_Test.adjustSize() # adjustSize() 메서드로 텍스트의 길이에 따라 라벨의 길이를 조절해주도록 합니다.


    def file_to_list(self):

        #컴퓨터 리스트
        file = open('Computer_name.txt', 'r', encoding='UTF8')
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

        #IP 리스트
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

        #MAC 리스트
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


    def initPingTest(self):  # 다중쓰레드 핑 테스트, 모든 컴퓨터들을 다 테스트해봄.
        for i in range(0, 10):
            ping_test_thread = threading.Thread(target=self.pingOk, args=(i,))  # args 튜플 끝 부분에 쉼표를 붙여줘야한다.
            ping_test_thread.setDaemon(True) # 데몬쓰레드는 메인 프로그램이 종료될때 자동으로 같이 종료한다.
            ping_test_thread.start()


    def pingOk(self, i):
        try:
            print(f'{i}' + self.list_of_IP[i])
            output = subprocess.check_output(
                "ping -{} 1 {}".format('n' if platform.system().lower() == "windows" else 'c', self.list_of_IP[i]),
                shell=True)
            self.computer_status[i].setText('작동 중')
            self.computer_status[i].setStyleSheet("color : darkgreen; font: bold 13px;")
        except Exception as e:
            self.computer_status[i].setText('연결 끊김')
            self.computer_status[i].setStyleSheet("color : gray ")
            return False
        return True


    def initTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.initPingTest)
        self.timer.start(60000)


    def initBtn(self):

        for i in range (0,10):
            self.list_of_packetClass.insert(i, send_packet_class(self.list_of_MAC[i]))
            self.computer_btn[i].clicked.connect(self.list_of_packetClass[i].send_packet)
            print('hihi' + self.list_of_packetClass[i].MAC)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ComputerListPrint()
    sys.exit(app.exec_())