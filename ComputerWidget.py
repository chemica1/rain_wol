from PyQt5.QtWidgets import *

class ComputerListPrint(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('ComputerList')

        #self.move(300, 300) #위젯을 스크린의 x=300px, y=300px의 위치로 이동시킵니다.
        #self.resize(500, 500) #위젯의 크기를 너비 400px, 높이 200px로 조절합니다.
        self.show()

