import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime, Qt
from ComputerWidget import ComputerListPrint

class MainWindow(QMainWindow): #메인윈도우에선 layout 못쓴다. 자체레이아웃을 갖고있기때문

    def __init__(self):
        super().__init__()

        ComputerListWidget = ComputerListPrint()
        self.setCentralWidget(ComputerListWidget) #센터 레이아웃에 꼭 추가해줘야한다.
        self.initTimer()
        self.initUI()


    def initUI(self):

        self.setWindowTitle('Wol for huliac')
        self.setWindowIcon(QIcon('huliacLogo.png'))


        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)


        menubar = self.menuBar()
        menubar.setNativeMenuBar(False) #macos에서 잘되라고 넣은 코드
        fileMenu = menubar.addMenu('&File') #앰퍼샌드&는 간편하게 단축기 설정해준거임 알프+F가됨
        fileMenu.addAction(exitAction)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.statusBar()
        self.statusBar().showMessage('Ready')

        #self.setGeometry(800, 200, 500, 500) # x, y, width, height
        self.resize(800, 300)
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


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())