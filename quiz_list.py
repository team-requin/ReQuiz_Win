import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *


class Main_Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('img/ReQuiz_logo_color.png'))
        self.setWindowTitle('Requiz')
        self.setFixedSize(1300, 800)
        self.show()

    def initUI(self):
        # label 선언 및 기본적인 설정
        line = QLabel('', self)
        line.move(0, 120)
        line.resize(1300, 515)


        label_logo = QLabel('', self)
        label_logo.resize(1300, 120)
        label_logo.setAlignment(Qt.AlignCenter)

        label_bottom_color = QLabel('', self)
        label_bottom_color.resize(1300, 165)
        label_bottom_color.move(0, 635)

        label_bottom1 = QLabel('Team Requin 소개 이용약관 개인정보처리방침 공지사항 이용가이드 일반이용문의', self)
        label_bottom1.move(380, 730)

        label_bottom2 = QLabel('XXX 대표 Xxx 사업자등록번호 XXX-XX-XXXX 통신판매업신고 XXXX-XXXX-XXXXX 주소 XXXXXXXXXX TEL XXX-XXXX-XXXX',
                               self)
        label_bottom2.move(130, 760)

        label_picture_white = QLabel(self)
        label_picture_color = QLabel(self)

        # label design 설정
        line.setStyleSheet("background-color:rgb(111, 168, 147);")

        label_logo.setStyleSheet("background-color:#40564e;"
                                 "color : white;"
                                 )

        label_bottom_color.setStyleSheet("background-color:white")

        # label font 설정

        font2 = label_logo.font()
        font3 = line.font()
        font4 = label_bottom1.font()
        font5 = label_bottom2.font()


        font2.setPointSize(30)
        font2.setBold(True)
        label_logo.setFont(font2)

        font3.setPointSize(70)
        line.setFont(font3)

        font4.setPointSize(9)
        label_bottom1.setFont(font4)

        font5.setPointSize(10)
        font5.setBold(True)
        label_bottom2.setFont(font5)

        # Qpixmap 선언 및 기본 설정
        pixmap_white = QPixmap('img/ReQuiz_logo_white.png')
        pixmap_white = pixmap_white.scaledToHeight(150)
        label_picture_white.move(570, -15)
        label_picture_white.setPixmap(pixmap_white)

        pixmap_color = QPixmap('img/ReQuiz_logo_color.png')
        pixmap_color = pixmap_color.scaledToHeight(80)
        label_picture_color.move(600, 640)
        label_picture_color.setPixmap(pixmap_color)

        profile_pix = QPixmap('img/200x200.png')
        profile_label = QLabel(self)
        profile_label.move(115, 200)
        profile_label.setPixmap(profile_pix)


        account_line = QLineEdit(self)
        account_line.setStyleSheet('display: block;'
                                   'margin: 20px auto;'
                                    'width: 220px;'
                                    'height: 40px;'
                                    'line-height: 40px;'
                                    'padding: 0 10px;'
                                    'outline: none;'
                                    'border: 1px solid #b1ffa7;')
        account_line.move(60, 420)

        nickname_line = QLineEdit(self)
        nickname_line.setStyleSheet('display: block;'
                                   'margin: 20px auto;'
                                    'width: 220px;'
                                    'height: 40px;'
                                    'line-height: 40px;'
                                    'padding: 0 10px;'
                                    'outline: none;'
                                    'border: 1px solid #b1ffa7;')
        nickname_line.move(60, 480)


        blank_label1 = QLabel('제목', self)
        blank_label1.resize(600, 72)
        blank_label1.setStyleSheet("border: 1px solid #b1ffa7;")
        blank_label1.move(450, 150)

        blank_label2 = QLabel('제목', self)
        blank_label2.resize(600, 72)
        blank_label2.setStyleSheet("border: 1px solid #b1ffa7;")
        blank_label2.move(450, 230)

        blank_label3 = QLabel('제목', self)
        blank_label3.resize(600, 72)
        blank_label3.setStyleSheet("border: 1px solid #b1ffa7;")
        blank_label3.move(450, 310)

        blank_label4 = QLabel('제목', self)
        blank_label4.resize(600, 72)
        blank_label4.setStyleSheet("border: 1px solid #b1ffa7;")
        blank_label4.move(450, 390)

        blank_label5 = QLabel('제목', self)
        blank_label5.resize(600, 72)
        blank_label5.setStyleSheet("border: 1px solid #b1ffa7;")
        blank_label5.move(450, 470)



        plus_btn = QPushButton('+플러스', self)
        plus_btn.resize(500, 50)
        plus_btn.setStyleSheet('border: 0;'
                                 'display: block;'
                                 'font-size: 15px;'
                                 'font-weight: bold;'
                                 'border-radius: 5px;'
                                 'background-color: #5dda72;')
        plus_btn.move(500, 570)


        modify_btn = QPushButton('수정', self)
        modify_btn.resize(220, 30)
        modify_btn.setStyleSheet("background-color: #94ff85;"
                                 "border-radius: 10px;"
                                 "color: #00791e;"
                                 )
        modify_btn.move(105, 575)



        modify_btn2_1 = QLabel('수정', self)
        modify_btn2_1.resize(120, 70)
        modify_btn2_1.setStyleSheet("border-radius : 5px;"
                                   "background-color: #b1ffa7;")
        modify_btn2_1.setAlignment(Qt.AlignCenter)
        modify_btn2_1.move(1100, 150)


        modify_btn2_2 = QLabel('수정', self)
        modify_btn2_2.resize(120, 70)
        modify_btn2_2.setStyleSheet("border-radius : 5px;"
                                   "background-color: #b1ffa7;")
        modify_btn2_2.setAlignment(Qt.AlignCenter)
        modify_btn2_2.move(1100, 230)


        modify_btn2_3= QLabel('수정', self)
        modify_btn2_3.resize(120, 70)
        modify_btn2_3.setStyleSheet("border-radius : 5px;"
                                   "background-color: #b1ffa7;")
        modify_btn2_3.setAlignment(Qt.AlignCenter)
        modify_btn2_3.move(1100, 310)


        modify_btn2_4= QLabel('수정', self)
        modify_btn2_4.resize(120, 70)
        modify_btn2_4.setStyleSheet("border-radius : 5px;"
                                   "background-color: #b1ffa7;")
        modify_btn2_4.setAlignment(Qt.AlignCenter)
        modify_btn2_4.move(1100, 390)


        modify_btn2_5= QLabel('수정', self)
        modify_btn2_5.resize(120, 70)
        modify_btn2_5.setStyleSheet("border-radius : 5px;"
                                   "background-color: #b1ffa7;")
        modify_btn2_5.setAlignment(Qt.AlignCenter)
        modify_btn2_5.move(1100, 470)


        # 레이아웃 적용
        layout = QVBoxLayout()
        layout.addWidget(line)
        layout.addWidget(label_logo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = Main_Window()
    sys.exit(app.exec_())