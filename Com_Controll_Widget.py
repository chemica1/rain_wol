from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class ComputerListPrint(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):



        self.c = Communicate() #새로운 시그널을 만듦
        self.c.closeApp.connect(self.close) #Communicate 클래스의 closeApp 시그널은 MyApp 클래스의 close() 슬롯에 연결됩니다.



        #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ그리드 시작ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        grid = QGridLayout()

        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        TestLabel = QLabel('Review:')
        grid.addWidget(TestLabel, 2, 0)
        """
             #QLabel 위젯은 텍스트 또는 이미지 라벨을 만들 때 쓰입니다. 사용자와 어떤 상호작용을 제공하지는 않습니다.
             #라벨은 기본적으로 수평 방향으로는 왼쪽, 수직 방향으로는 가운데 정렬이지만 setAlignment() 메서드를 통해 조절할 수 있습니다.
             #TestLabel.setAlignment(Qt.AlignCenter) #setAlignment() 메서드로 라벨의 배치를 설정할 수 있습니다. Qt.AlignCenter로 설정해주면 수평, 수직 방향 모두 가운데 위치하게 됩니다. Qt.AlignVCenter <- 이건 수직방향으로 가운데
             :return: 
        """
        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)




        #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ버튼 시작ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

        okButton = QPushButton('OK', self) #뒤에 self는 속할 부모클래스를 지정해줌
        okButton.setCheckable(True)
        cancelButton = QPushButton('Cancel')
        """
        #선택되거나 선택되지 않은 상태를 유지할 수 있게 됩니다. (=눌럿을때 파란색되고 유지되느냐?)
        #okButton.toggle() #메서드를 호출하면 버튼의 상태가 바뀌게 됩니다. 따라서 이 버튼은 프로그램이 시작될 때 선택되어 있습니다.
        #okButton.setEnabled(False) #False로 설정하면, 버튼을 사용할 수 없게 됩니다.
        """


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)
        """
        레이아웃에 담아 수평적으로 정리하는 파트
        """

        #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ라디오 버튼ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

        rbtn1 = QRadioButton('First Button', self)
        rbtn1.setChecked(True)

        rbtn2 = QRadioButton(self)
        rbtn2.setText('Second Button')

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(rbtn1)
        hbox2.addWidget(rbtn2)
        hbox2.addStretch(1)

        """
        라디오 버튼은 일반적으로 사용자에게 여러 개 중 하나의 옵션을 선택하도록 할 때 사용됩니다. 
        그래서 한 위젯 안에 여러 라디오 버튼은 기본적으로 autoExclusive로 설정되어 있습니다. 하나의 버튼을 선택하면 나머지 버튼들은 선택 해제가 됩니다.
        체크 박스와 마찬가지로 버튼의 상태가 바뀔 때, toggled() 시그널이 발생합니다. 또한 특정 버튼의 상태를 가져오고 싶을 때, isChecked() 메서드를 사용할 수 있습니다.
        """


        #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ콤보박스 & QLineEdit ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

        self.Label_Combo = QLabel('Option1', self)
        cb = QComboBox(self)
        cb.addItem('안녕')
        cb.addItem('메롱')
        cb.addItem('maple')
        cb.activated[str].connect(self.onActivated) #변경될때 그 왼쪽에 껏도 자기 이름으로 바꺼쥼


        self.Label_Test = QLabel(self)
        qle = QLineEdit(self)
        qle.textChanged[str].connect(self.onChanged) #qle의 텍스트가 바뀌면, onChanged() 메서드를 호출합니다.


        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.Label_Combo)
        hbox3.addWidget(cb)
        hbox3.addStretch(1)

        hbox3.addWidget(self.Label_Test)
        hbox3.addWidget(qle)
        hbox3.addStretch(1)


        #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ수직하게 정리중ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addStretch(1)

        self.setLayout(vbox)

        #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


        self.setWindowTitle('ComputerList')
        self.show()


    def onActivated(self, text):

        self.Label_Combo.setText(text)
        self.Label_Combo.adjustSize()

    def onChanged(self, text):

        self.Label_Test.setText(text)
        self.Label_Test.adjustSize() # adjustSize() 메서드로 텍스트의 길이에 따라 라벨의 길이를 조절해주도록 합니다.


    def mousePressEvent(self, e): #mousePressEvent 이벤트 핸들러를 사용해서, 마우스를 클릭했을 때 closeApp 시그널이 방출되도록 했습니다.

        self.c.closeApp.emit()


class Communicate(QObject): #pyqtSignal()을 가지고 Communicate 클래스의 속성으로서 closeApp이라는 시그널을 하나 만들었습니다.

    closeApp = pyqtSignal()