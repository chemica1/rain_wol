import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime, Qt
from Com_Controll_Widget import ComputerListPrint
from Com_Info_Widget import SetComputer

class MainWindow(QMainWindow): #메인윈도우에선 layout 못쓴다. 자체레이아웃을 갖고있기때문

    def __init__(self):
        super().__init__()


        ComputerListWidget = ComputerListPrint()
        self.setCentralWidget(ComputerListWidget) #센터 레이아웃에 꼭 추가해줘야한다.

        self.initTimer()
        self.initUI()


    def initUI(self):

        self.setWindowTitle('WOL for huliac')
        self.setWindowIcon(QIcon('huliacLogo.png'))


        showComputerList = QAction(QIcon('poweron.png'), 'Power On', self)
        showComputerList.setShortcut('Ctrl+O')
        showComputerList.setStatusTip('현재 컴퓨터 상태를 조작합니다.')
        showComputerList.triggered.connect(self.showComputerList)
        self.toolbar = self.addToolBar('showComputerList')
        self.toolbar.addAction(showComputerList)


        changeComputerList = QAction(QIcon('edit.png'), 'changeComputerList', self)
        changeComputerList.setShortcut('Ctrl+T')
        changeComputerList.setStatusTip('컴퓨터 정보를 변경합니다.')
        changeComputerList.triggered.connect(self.showSetComputerWidget)
        self.toolbar = self.addToolBar('changeComputerList')
        self.toolbar.addAction(changeComputerList)


        #menubar = self.menuBar()
        #menubar.setNativeMenuBar(False) #mac os에서 잘되라고 넣은 코드
        #fileMenu = menubar.addMenu('&File') #앰퍼샌드&는 간편하게 단축기 설정해준거임 알프+F가됨
        #fileMenu.addAction(exitAction)


        self.statusBar()
        self.statusBar().showMessage('Ready')



        """
        #self.setGeometry(800, 200, 500, 500) # x, y, width, height
        #self.move(300, 300) #위젯을 스크린의 x=300px, y=300px의 위치로 이동시킵니다.
        #self.resize(500, 500) #위젯의 크기를 너비 400px, 높이 200px로 조절합니다.
        """

        self.resize(800, 400)
        self.initWindowWhere()
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate) + ' '+self.time.toString()) #시간표시
        self.show()


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


    def showSetComputerWidget(self):

        SettingComputer = SetComputer()
        self.setCentralWidget(SettingComputer) #센터 레이아웃에 꼭 추가해줘야한다.






    """
    def keyPressEvent(self, e): #이렇게 미리 만들어진 이벤트 핸들러가 많다.

        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_F:
            self.showFullScreen()
        elif e.key() == Qt.Key_N:
            self.showNormal()
    """


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())