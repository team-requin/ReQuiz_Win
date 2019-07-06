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

        label_main = QLabel('REQUIZ', self)
        label_main.move(450, 210)

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
        label_main.setStyleSheet("color : white;"
                                 "font:65pt Segoe UI Black;"
                                 )
        label_bottom_color.setStyleSheet("background-color:white")

        # label font 설정
        font1 = label_main.font()
        font2 = label_logo.font()
        font3 = line.font()
        font4 = label_bottom1.font()
        font5 = label_bottom2.font()

        font1.setPointSize(60)
        font1.setBold(True)
        label_main.setFont(font1)

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

        # QLineEdit 선언 및 기본적인 설정
        LineEdit_search_id = QLineEdit(self)
        LineEdit_search_id.resize(560, 60)
        LineEdit_search_id.move(370, 380)

        # QLineEdit design 설정
        LineEdit_search_id.setPlaceholderText('please enter the ID to search')
        LineEdit_search_id.setStyleSheet("border: 1px solid #ffaef8;"
                                         "border-radius: 10px;"
                                         "font-size: 25px;")

        # button 선언 및 기본적인 설정
        button_search_id = QPushButton('Search', self)
        button_login = QPushButton("로그인", self)
        button_logout = QPushButton('로그아웃', self)

        button_search_id.resize(560, 50)
        button_search_id.move(370, 460)

        button_login.resize(100, 50)
        button_login.move(1050, 35)
        button_login.clicked.connect(self.onClick_login)

        button_logout.resize(100, 50)
        button_logout.move(1170, 35)

        # button design 설정
        button_login.setStyleSheet("QPushButton:hover{background-color: #5d877a; border-radius: 15px;}"
                                   "QPushButton{background-color: rgb(91, 124, 112);"
                                   "border-radius: 15px;"
                                   "color: white;}")

        button_logout.setStyleSheet("QPushButton:hover{background-color: #5d877a; border-radius: 15px;}"
                                    "QPushButton{background-color: rgb(91, 124, 112);"
                                    "border-radius: 15px;"
                                    "color: white;}")

        button_search_id.setStyleSheet("QPushButton:hover{background-color: rgb(0, 0, 0, 40%); border-radius: 15px;}"
                                       "QPushButton{background-color: #40564e;"
                                       "border-radius: 15px;"
                                       "color: white;}")

        # 레이아웃 적용
        layout = QVBoxLayout()
        layout.addWidget(line)
        layout.addWidget(label_main)
        layout.addWidget(LineEdit_search_id)
        layout.addWidget(label_logo)

    def onClick_login(self):
        self.main_to_login = Login_Window()

class Login_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setFixedSize(400, 550)
        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon('img/ReQuiz_logo_color'))
        self.show()

    def initUI(self):
        #QLabel 선언 및 기본적인 설정
        label_background = QLabel('', self)
        label_background.resize(400, 550)

        label_main = QLabel('LOGIN', self)
        label_main.move(100, 50)

        label_image = QLabel(self)

        #QLabel design 설정
        label_background.setStyleSheet("background-color: #7a978d")
        label_main.setStyleSheet("font: 70px MS PGothic;")


        #QLineEdit 선언 및 기본적인 설정
        LineEdit_id = QLineEdit(self)
        LineEdit_pw = QLineEdit(self)

        LineEdit_id.resize(330, 50)
        LineEdit_id.move(35, 170)
        LineEdit_id.setPlaceholderText("ID")

        LineEdit_pw.resize(330, 50)
        LineEdit_pw.move(35, 240)
        LineEdit_pw.setPlaceholderText('Password')
        LineEdit_pw.setEchoMode(QLineEdit.Password)

        #QLineEdit design 설정
        LineEdit_id.setStyleSheet("border-radius: 15px;"
                                  "font: 17px;"
                                  "font-weight: bold;")

        LineEdit_pw.setStyleSheet("border-radius: 15px;"
                                  "font: 17px;"
                                  "font-weight: bold;")

        #QPushButton 선언 및 기본 설정
        Button_login = QPushButton('login', self)
        Button_login.resize(200, 50)
        Button_login.move(95, 330)
        Button_login.clicked.connect(self.func_close_id)

        Button_new = QPushButton('회원가입', self)
        Button_new.move(154, 400)
        Button_new.clicked.connect(self.func_close_new)
        Button_new.clicked.connect(self.onClick_new)

        #QPushButton design 설정
        Button_login.setStyleSheet("QPushButton:hover{border-radius: 15px; background-color: #C9CFCD;}"
                                   "QPushButton{border-radius: 15px; background-color: #DDDDDD; font: 25px; font-weight: bold;}")
        Button_new.setStyleSheet("color: #37573B; background-color: #7a978d; border-width: 1px; border-style: solid;border-color: #7a978d #7a978d #37573B #7a978d;"
                                 "font: 20px; font-weight: bold;")

        #QPixmap 선언 및 기본 설정
        pixmap_color = QPixmap('img/ReQuiz_logo_black.png')
        pixmap_color = pixmap_color.scaledToHeight(150)
        label_image.move(123, 405)
        label_image.setPixmap(pixmap_color)

    def func_close_id(self):
        self.close()
        QMessageBox.about(self, "Login", "Login Successful!")

    def func_close_new(self):
        self.close()

    def onClick_new(self):
        self.login_to_new = New_Window()

class New_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setFixedSize(400, 550)
        self.setWindowTitle('New')
        self.setWindowIcon(QIcon('img/ReQuiz_logo_color'))
        self.show()

    def initUI(self):
        # QLabel 선언 및 기본적인 설정
        label_background = QLabel('', self)
        label_background.resize(400, 550)

        label_main = QLabel('SIGN UP', self)
        label_main.move(105, 30)

        # QLabel design 설정
        label_background.setStyleSheet("background-color: #7a978d")
        label_main.setStyleSheet("font: 50px MS PGothic; color: white;")

        # QLineEdit 선언 및 기본적인 설정
        LineEdit_name = QLineEdit(self)
        LineEdit_id = QLineEdit(self)
        LineEdit_pw = QLineEdit(self)
        LineEdit_pw_chek = QLineEdit(self)

        LineEdit_name.resize(250, 50)
        LineEdit_name.move(35, 120)
        LineEdit_name.setPlaceholderText("Nickname")

        LineEdit_id.resize(250, 50)
        LineEdit_id.move(35, 190)
        LineEdit_id.setPlaceholderText('ID')
        LineEdit_id.setEchoMode(QLineEdit.Password)

        LineEdit_pw.resize(330, 50)
        LineEdit_pw.move(35, 270)
        LineEdit_pw.setPlaceholderText('Password')
        LineEdit_pw.setEchoMode(QLineEdit.Password)

        LineEdit_pw_chek.resize(330, 50)
        LineEdit_pw_chek.move(35, 340)
        LineEdit_pw_chek.setPlaceholderText('Confirm Password')
        LineEdit_pw_chek.setEchoMode(QLineEdit.Password)

        # QLineEdit design 설정
        LineEdit_name.setStyleSheet("border-radius: 15px;"
                                    "font: 17px;"
                                    "font-weight: bold;"
                                    )

        LineEdit_id.setStyleSheet("border-radius: 15px;"
                                  "font: 17px;"
                                  "font-weight: bold;")

        LineEdit_pw.setStyleSheet("border-radius: 15px;"
                                  "font: 17px;"
                                  "font-weight: bold;")

        LineEdit_pw_chek.setStyleSheet("border-radius: 15px;"
                                       "font: 17px;"
                                       "font-weight: bold;")

        # QPushButton 선언 및 기본 설정
        Button_new = QPushButton('Sign up', self)
        Button_new.resize(200, 50)
        Button_new.move(95, 430)
        Button_new.clicked.connect(self.func_close)

        Button_check_name = QPushButton('Check', self)
        Button_check_name.resize(70, 50)
        Button_check_name.move(295, 120)

        Button_check_id = QPushButton('Check', self)
        Button_check_id.resize(70, 50)
        Button_check_id.move(295, 190)

        # QPushButton design 설정
        Button_new.setStyleSheet("QPushButton:hover{border-radius: 15px; background-color: #C9CFCD;}"
                                   "QPushButton{border-radius: 15px; background-color: #DDDDDD; font: 25px; font-weight: bold;}")
        Button_check_name.setStyleSheet(
            "QPushButton:hover{border-radius: 5px; background-color: #40564e; font: 15px; color: white; font-weight: bold;}"
            "QPushButton{border-radius: 5px; background-color: #4C635B; font: 15px; color: white; font-weight: bold;}")
        Button_check_id.setStyleSheet(
            "QPushButton:hover{border-radius: 5px; background-color: #40564e; font: 15px; color: white; font-weight: bold;}"
            "QPushButton{border-radius: 5px; background-color: #4C635B; font: 15px; color: white; font-weight: bold;}")

    def func_close(self):
        self.close()
        QMessageBox.about(self, "Sign up", "Sign up Successful!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = Main_Window()
    sys.exit(app.exec_())