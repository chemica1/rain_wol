from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class ComputerListPrint(QWidget):


    def __init__(self):

        super().__init__()

        self.list_of_name = []
        self.list_of_IP = []
        self.list_of_MAC = []
        self.file_to_list()

        self.computer_checkbox = []  #원소가 없는 상태에서 = 연산자로 대입 불가능함. append나 insert 둘 중 하나로 해야됨.
        self.computer_status = []
        self.computer_btn = []

        self.initUI()


    def initUI(self):

        self.whole_box = QGroupBox('체크된 컴퓨터 제어')

        self.on_button = QPushButton('Power on', self) #뒤에 self는 속할 부모클래스를 지정해줌
        self.on_button.setStyleSheet("background-color: gray; border-style: outset; border-width: 2px; border-radius: 10px; border-color: gray; font: bold 14px;  padding: 6px; color : white; ")
        self.checkbox_button = QPushButton('전체 체크', self)
        self.pingtest_button = QPushButton('핑 테스트', self)

        self.whole_layout = QHBoxLayout()
        self.whole_layout.addStretch(1)
        self.whole_layout.addWidget(self.checkbox_button)
        self.whole_layout.addStretch(1)
        self.whole_layout.addWidget(self.on_button)
        self.whole_layout.addStretch(1)
        self.whole_layout.addWidget(self.pingtest_button)
        self.whole_layout.addStretch(1)
        self.whole_box.setLayout(self.whole_layout)

        self.power_box = QGroupBox('개별 제어 & 모니터링')

        for i in range(0, 10):
            self.computer_checkbox.insert(i, QCheckBox(self.list_of_name[i], self))
            self.computer_status.insert(i, QLabel('ㅡㅡ'))
            self.computer_btn.insert(i, QPushButton('Power on', self))

        self.computer_layout = QGridLayout()
        for i in range(0, 10):
            self.computer_layout.addWidget(self.computer_checkbox[i], i, 0)
            self.computer_layout.addWidget(self.computer_status[i], i, 1)
            self.computer_layout.addWidget(self.computer_btn[i], i, 2)
        self.power_box.setLayout(self.computer_layout)

        self.layout = QGridLayout()
        self.layout.addWidget(self.whole_box, 0, 0)
        self.layout.addWidget(self.power_box, 1, 0)
        self.setLayout(self.layout)


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


        """
        def mousePressEvent(self, e): #mousePressEvent 이벤트 핸들러를 사용해서, 마우스를 클릭했을 때 closeApp 시그널이 방출되도록 했습니다.

            self.c.closeApp.emit()
        """

class Communicate(QObject): #pyqtSignal()을 가지고 Communicate 클래스의 속성으로서 closeApp이라는 시그널을 하나 만들었습니다.

    closeApp = pyqtSignal()