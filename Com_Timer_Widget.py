import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class ComputerTimePrint(QWidget):

    def __init__(self):
        super().__init__()
        self.dir_path = os.getcwd()

        self.init_quit_time()
        self.list_of_name = []
        self.list_of_startTime = []
        self.file_to_list()
        self.start_time_comboBox_index = 0

        self.initUI()
        self.init_INFO()


    def initUI(self):

        # 현재 스케줄
        self.txt_group = QGroupBox('컴퓨터 시작 시간 설정')

        self.text_label_name = QLabel('이름')
        self.text_label_time = QLabel('시작시간')
        self.name_txt = QPlainTextEdit()
        self.start_time_txt = QPlainTextEdit()

        self.txt_grid = QGridLayout()
        self.txt_grid.addWidget(self.text_label_name, 0, 0)
        self.txt_grid.addWidget(self.text_label_time, 0, 1)
        self.txt_grid.addWidget(self.name_txt, 1, 0)
        self.txt_grid.addWidget(self.start_time_txt, 1, 1)

        self.computer_starttime_combo = QComboBox()
        self.computer_starttime_combo.addItem('컴퓨터 목록')
        for i in self.list_of_name:
            self.computer_starttime_combo.addItem(i)
        self.start_time_lineEdit = QLineEdit()
        self.start_time_label = QLabel('<시작시간 변경>')
        self.start_time_label.setAlignment(Qt.AlignHCenter)
        self.start_time_lineEdit.setPlaceholderText('시작 시간')
        self.start_time_save_btn = QPushButton('저장', self)
        self.start_time_save_btn.setEnabled(False)

        self.timer_controller = QVBoxLayout()
        self.timer_controller.addStretch()
        self.timer_controller.addWidget(self.start_time_label)
        self.timer_controller.addWidget(self.computer_starttime_combo)
        self.timer_controller.addWidget(self.start_time_lineEdit)
        self.timer_controller.addWidget(self.start_time_save_btn)

        self.lay = QHBoxLayout()
        self.lay.addLayout(self.txt_grid)
        self.lay.addLayout(self.timer_controller)
        self.txt_group.setLayout(self.lay)

        # 종료시간 박스
        self.end_time_group = QGroupBox('컴퓨터 일괄종료 시간 설정')
        self.end_time_label = QLabel('종료시간 :')
        self.end_time_timeedit = QTimeEdit(self)
        self.end_time_timeedit.setTime(QTime(int(self.quit_time[0]), int(self.quit_time[1])))
        self.end_time_timeedit.setDisplayFormat('hh:mm')
        self.end_time_save_btn = QPushButton('저장', self)

        self.end_time_layout = QHBoxLayout()
        self.end_time_layout.addWidget(self.end_time_label)
        self.end_time_layout.addWidget(self.end_time_timeedit)
        self.end_time_layout.addWidget(self.end_time_save_btn)
        self.end_time_group.setLayout(self.end_time_layout)

        # activated.connect
        self.computer_starttime_combo.activated.connect(self.combo_changed)
        self.start_time_save_btn.clicked.connect(self.start_time_save_btn_clicked)
        self.end_time_save_btn.clicked.connect(self.end_time_save_btn_clicked)

        #전체 구조
        self.layout = QGridLayout()
        self.layout.addWidget(self.txt_group, 0, 0)
        self.layout.addWidget(self.end_time_group, 1, 0)
        self.setLayout(self.layout)


    def init_INFO(self):

        with open(f'{self.dir_path}\\Computer_name.txt', 'r', encoding='UTF8') as fp_name:
            self.name_txt.setPlainText(fp_name.read())

        with open(f'{self.dir_path}\\Computer_start_time.txt', 'r', encoding='UTF8') as fp_start_time:
            self.start_time_txt.setPlainText(fp_start_time.read())


    def combo_changed(self, index):
        print(index)
        if not index == 0:
            self.start_time_save_btn.setEnabled(True)
            self.start_time_lineEdit.setInputMask('99:99:99; ')
            self.start_time_comboBox_index = index


    def start_time_save_btn_clicked(self):

        time = str(self.start_time_lineEdit.text()) #착각하면 안된다. 여기서 나오는 반환값은 String이 아니라 QString이다...
        #temp = int(name[0])  #Qstring을 int로 바꾼다. #7/19 여기 수정해야됨. 10이 1로되는현상. #7/25 수정함 전역변수를 사용해서
        index = self.start_time_comboBox_index - 1
        time.replace(" ", "")
        self.save_newInfo('start_time', index, time)
        self.init_INFO()


    def save_newInfo(self, file, index, newInfo):

        if file == 'start_time':
            self.list_of_startTime[index] = newInfo
            with open(f'{self.dir_path}\\Computer_{file}.txt', 'w', encoding='UTF8') as fp:
                for i in self.list_of_startTime:
                    data = i
                    fp.write(data + '\n')


    def fileSetting(self, index):

        f = open(f'{self.dir_path}\\Computer_name.txt', 'r', encoding='UTF8').read()
        self.name_txt.setPlainText(f)
        self.IP_txt.setPlainText(f)
        self.MAC_txt.setPlainText(f)

        with open(f'{self.dir_path}\\Computer_name.txt', 'r', encoding='UTF8') as fp:
            for i, line in enumerate(fp):
                if i == (index-2):
                    self.input_mask_name.setText(fp.readline())
                elif i > 10:
                    break


    def file_to_list(self):

        #컴퓨터 리스트
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

        #IP 리스트
        file = open(f'{self.dir_path}\\Computer_start_time.txt', 'r', encoding='UTF8')
        while (1):
            line = file.readline()
            try:
                escape = line.index('\n')
            except:
                escape = len(line)
            if line:
                self.list_of_startTime.append(line[0:escape])
            else:
                break
        file.close()


    def init_quit_time(self):

        f = open("Computer_time.txt", 'r')
        temp = f.read()
        temp2 = temp.split(':')
        self.quit_time = temp2
        print(f'현재 설정된 종료시간은 {self.quit_time}입니다.')
        f.close()


    def end_time_save_btn_clicked(self):

        temp = self.end_time_timeedit.text()
        with open('Computer_time.txt', 'w', encoding='UTF8') as fp:
            fp.write(temp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ComputerTimePrint()
    sys.exit(app.exec_())