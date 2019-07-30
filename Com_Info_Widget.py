import sys, os
from PyQt5.QtWidgets import *


class ComputerInfoPrint(QWidget):

    def __del__(self):
        print("2가 없어졌어요!")

    def __init__(self):
        super().__init__()
        self.dir_path = os.getcwd()
        self.list_of_name = []
        self.list_of_IP = []
        self.list_of_MAC = []
        self.file_to_list()
        self.input_mask_index = 0

        self.initUI()
        self.init_INFO()


    def initUI(self):

        # IP MAC 변경
        self.input_mask_group = QGroupBox('IP, MAC 변경')

        self.input_mask_label = QLabel('전시 컴퓨터 목록 :')
        self.input_mask_cb = QComboBox()
        self.input_mask_cb.addItem('목록')
        for i in self.list_of_name:
            self.input_mask_cb.addItem(i)
        self.input_mask_name = QLineEdit()
        self.input_mask_IP = QLineEdit()
        self.input_mask_MAC = QLineEdit()
        self.save_btn = QPushButton('저장', self)
        self.save_btn.setEnabled(False)

        self.input_mask_name.setPlaceholderText('컴퓨터 이름')
        self.input_mask_IP.setPlaceholderText('IP 주소')
        self.input_mask_MAC.setPlaceholderText('MAC 주소')

        self.input_mask_layout = QGridLayout()
        self.input_mask_layout.addWidget(self.input_mask_label, 0, 0)
        self.input_mask_layout.addWidget(self.input_mask_cb, 0, 1)
        self.input_mask_layout.addWidget(self.save_btn, 0, 2)
        self.input_mask_layout.addWidget(self.input_mask_name, 1, 0)
        self.input_mask_layout.addWidget(self.input_mask_IP, 1, 1)
        self.input_mask_layout.addWidget(self.input_mask_MAC, 1, 2)

        self.input_mask_group.setLayout(self.input_mask_layout)

        # IP MAC 정보
        self.txt_group = QGroupBox('현재 IP, MAC 정보')

        self.text_label_name = QLabel('이름')
        self.text_label_IP = QLabel('IP')
        self.text_label_MAC = QLabel('MAC')
        self.name_txt = QPlainTextEdit()
        self.IP_txt = QPlainTextEdit()
        self.MAC_txt = QPlainTextEdit()

        self.txt_grid = QGridLayout()
        self.txt_grid.addWidget(self.text_label_name, 0, 0)
        self.txt_grid.addWidget(self.text_label_IP, 0, 5)
        self.txt_grid.addWidget(self.text_label_MAC, 0, 10)
        self.txt_grid.addWidget(self.name_txt, 1, 0)
        self.txt_grid.addWidget(self.IP_txt, 1, 5)
        self.txt_grid.addWidget(self.MAC_txt, 1, 10)
        self.txt_group.setLayout(self.txt_grid)

        # activated.connect
        self.input_mask_cb.activated.connect(self.input_mask_changed)
        self.save_btn.clicked.connect(self.btn_clicked)

        #전체 구조
        self.layout = QGridLayout()
        self.layout.addWidget(self.txt_group, 0, 0)
        self.layout.addWidget(self.input_mask_group, 1, 0)
        self.setLayout(self.layout)

        self.setWindowTitle('Line Editor')


    def init_INFO(self):

        with open(f'{self.dir_path}\\Computer_name.txt', 'r', encoding='UTF8') as fp_name:
            self.name_txt.setPlainText(fp_name.read())

        with open(f'{self.dir_path}\\Computer_IP.txt', 'r', encoding='UTF8') as fp_IP:
            self.IP_txt.setPlainText(fp_IP.read())

        with open(f'{self.dir_path}\\Computer_MAC.txt', 'r', encoding='UTF8') as fp_MAC:
            self.MAC_txt.setPlainText(fp_MAC.read())


    def input_mask_changed(self, index):
        print(index)
        if not index == 0:
            self.save_btn.setEnabled(True)
            self.input_mask_name.setInputMask(f'{index}. xxxxxxxxxxxx; ')
            self.input_mask_IP.setInputMask('xxx.xxx.xxx.xxx; ')
            self.input_mask_MAC.setInputMask('>xx.xx.xx.xx.xx.xx;_ ')
            self.input_mask_index = index


    def btn_clicked(self):
        name = self.input_mask_name.text() #착각하면 안된다. 여기서 나오는 반환값은 String이 아니라 QString이다...
        IP = self.input_mask_IP.text()
        MAC = str(self.input_mask_MAC.text())
        temp = len(MAC)
        IP.replace(" ", "")
        #temp = int(name[0])  #Qstring을 int로 바꾼다. #7/19 여기 수정해야됨. 10이 1로되는현상. #7/25 수정함 전역변수를 사용해서
        index = self.input_mask_index - 1

        if temp > 8 :
            self.save_newInfo('MAC', index, MAC)
        else:
            self.save_newInfo('MAC', index, '00.00.00.00.00.00')
        self.save_newInfo('name', index, name)
        self.save_newInfo('IP', index, IP)

        self.init_INFO()


    def save_newInfo(self, file, index, newInfo):

        if file == 'MAC':
            self.list_of_MAC[index] = newInfo
            with open(f'{self.dir_path}\\Computer_{file}.txt', 'w', encoding='UTF8') as fp:
                for i in self.list_of_MAC:
                    data = i
                    fp.write(data+'\n')

        if file == 'name':
            self.list_of_name[index] = newInfo
            with open(f'{self.dir_path}\\Computer_{file}.txt', 'w', encoding='UTF8') as fp:
                for i in self.list_of_name:
                    data = i
                    fp.write(data + '\n')

        if file == 'IP':
            self.list_of_IP[index] = newInfo
            with open(f'{self.dir_path}\\Computer_{file}.txt', 'w', encoding='UTF8') as fp:
                for i in self.list_of_IP:
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

        #MAC 리스트
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ComputerInfoPrint()
    sys.exit(app.exec_())