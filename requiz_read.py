import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

class Quiz(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('img/requin_blue.png'))
        self.setWindowTitle('Requiz')
        self.setFixedSize(1300, 800)
        self.show()

    def initUI(self):
        line = QLabel('', self)
        line.move(0, 120)
        line.resize(1300, 680)

        label_picture_white = QLabel(self)

        label_logo = QLabel('', self)
        label_logo.resize(1300, 120)
        label_logo.setAlignment(Qt.AlignCenter)

        # label design 설정
        line.setStyleSheet("background-color:rgb(111, 168, 147);")

        label_logo.setStyleSheet("background-color:#40564e;"
                                 "color : white;")

        # label font 설정
        font1 = label_logo.font()
        font2 = line.font()

        font1.setPointSize(30)
        font1.setBold(True)
        label_logo.setFont(font1)

        font2.setPointSize(70)
        line.setFont(font2)

        label1_qes = QLabel('● Requin은 무엇일까요?\t\t\t\t\t\t\t\t\t', self)
        label1_qes.move(200, 200)

        label1_qes.setStyleSheet("color: black;"
                               "background-color: #FFFFFF;"
                               "border-style: soild;"
                               "border-width: 25px;"
                                "font-weight: bold;")


        label1_ans = QLabel('\t▶ Requin은 대덕소프트웨어마이스터고등학교 5기 학생들이 만든 팀입니다!\t\t\t\t', self)
        label1_ans.move(200, 300)

        morebtn = QPushButton('더보기', self)
        morebtn.resize(500, 50)
        morebtn.move(400, 700)


        label1_ans.setStyleSheet("color: black;"
                                 "background-color: #FFFFFF;"
                                 "border-style: soild;"
                                 "border-width: 25px;"
                                 "font-weight: bold;")

        morebtn.setStyleSheet("QPushButton:hover{border-radius: 10px; background-color: #2F9D27;}"
                                 "QPushButton{border-radius: 10px; background-color: #22741C; font: 15px; color: white;"
                                    "font-weight: bold;}")

        label_picture_white = QLabel(self)
        pixmap_white = QPixmap('img/requin_white.png')
        pixmap_white = pixmap_white.scaledToHeight(150)
        label_picture_white.move(570, -15)
        label_picture_white.setPixmap(pixmap_white)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Quiz()
    sys.exit(app.exec_())