import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Loding_Widget(QWidget):
    def __del__(self):
        print("3가 없어졌어요!")

    def __init__(self, text="로딩중..."):
        super().__init__()
        self.setWindowTitle("Messages")

        self.setLayout(QVBoxLayout())
        self._layout = self.layout()

        self._gif = QLabel()
        movie = QMovie("loading.gif")
        self._gif.setMovie(movie)
        movie.start()
        self._layout.addWidget(self._gif)


        self._message = QLabel()
        self._message.setText(text)
        self._message.setAlignment(Qt.AlignHCenter)
        self._layout.addWidget(self._message)
        self.setObjectName('Message_Window')

        self._layout.setSpacing(3)
        self._layout.setAlignment(Qt.AlignCenter)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Loding_Widget()
    sys.exit(app.exec_())