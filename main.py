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
        line.resize(1300, 680)

        self.label_main = QLabel('REQUIZ', self)
        self.label_main.move(450, 260)

        label_logo = QLabel('', self)
        label_logo.resize(1300, 120)
        label_logo.setAlignment(Qt.AlignCenter)

        label_picture_white = QLabel(self)

        # label design 설정
        line.setStyleSheet("background-color:rgb(111, 168, 147);")

        label_logo.setStyleSheet("background-color:#40564e;"
                                 "color : white;"
                                 )
        self.label_main.setStyleSheet("color : white;"
                                 "font:65pt Segoe UI Black;"
                                 )

        # label font 설정
        font1 = self.label_main.font()
        font2 = label_logo.font()
        font3 = line.font()

        font1.setPointSize(60)
        font1.setBold(True)
        self.label_main.setFont(font1)

        font2.setPointSize(30)
        font2.setBold(True)
        label_logo.setFont(font2)

        font3.setPointSize(70)
        line.setFont(font3)

        # Qpixmap 선언 및 기본 설정
        pixmap_white = QPixmap('img/ReQuiz_logo_white.png')
        pixmap_white = pixmap_white.scaledToHeight(150)
        label_picture_white.move(570, -15)
        label_picture_white.setPixmap(pixmap_white)

        # QLineEdit 선언 및 기본적인 설정
        self.LineEdit_search_id = QLineEdit(self)
        self.LineEdit_search_id.resize(560, 60)
        self.LineEdit_search_id.move(370, 450)

        # QLineEdit design 설정
        self.LineEdit_search_id.setPlaceholderText('please enter the ID to search')
        self.LineEdit_search_id.setStyleSheet("border: 1px solid #ffaef8;"
                                         "border-radius: 10px;"
                                         "font-size: 25px;")

        # button 선언 및 기본적인 설정
        self.button_search_id = QPushButton('Search', self)
        self.button_login = QPushButton("로그인", self)
        self.button_logout = QPushButton('로그아웃', self)

        self.button_search_id.resize(560, 50)
        self.button_search_id.move(370, 530)
        self.button_search_id.clicked.connect(self.click_search)

        self.button_login.resize(100, 50)
        self.button_login.move(1050, 35)
        self.button_login.clicked.connect(self.onClick_login)

        self.button_logout.resize(100, 50)
        self.button_logout.move(1170, 35)

        # button design 설정
        self.button_login.setStyleSheet("QPushButton:hover{background-color: #5d877a; border-radius: 15px;}"
                                   "QPushButton{background-color: rgb(91, 124, 112);"
                                   "border-radius: 15px;"
                                   "color: white;}")

        self.button_logout.setStyleSheet("QPushButton:hover{background-color: #5d877a; border-radius: 15px;}"
                                    "QPushButton{background-color: rgb(91, 124, 112);"
                                    "border-radius: 15px;"
                                    "color: white;}")

        self.button_search_id.setStyleSheet("QPushButton:hover{background-color: rgb(0, 0, 0, 40%); border-radius: 15px;}"
                                       "QPushButton{background-color: #40564e;"
                                       "border-radius: 15px;"
                                       "color: white;}")

        # 레이아웃 적용z

    def onClick_login(self):
        self.main_to_login = Login_Window()

    def click_search(self):
        self.button_search_id.close()
        self.button_login.close()
        self.LineEdit_search_id.close()
        self.button_logout.close()
        self.label_main.close()

        self.initUI_list()

    def initUI_list(self):
        self.setWindowTitle('List')

        profile_pix = QPixmap('img/200x200.png')
        profile_label = QLabel(self)
        profile_label.move(115, 200)
        profile_label.setPixmap(profile_pix)
        profile_label.show()

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
        account_line.show()

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
        nickname_line.show()

        blank_label1 = QLabel('제목', self)
        blank_label1.resize(600, 72)
        blank_label1.setStyleSheet("border: 1px solid #b1ffa7;")
        blank_label1.move(450, 150)
        blank_label1.show()

        blank_label2 = QLabel('제목', self)
        blank_label2.resize(600, 72)
        blank_label2.setStyleSheet("border: 1px solid #b1ffa7;")
        blank_label2.move(450, 230)
        blank_label2.show()

        blank_label3 = QLabel('제목', self)
        blank_label3.resize(600, 72)
        blank_label3.setStyleSheet("border: 1px solid #b1ffa7;")
        blank_label3.move(450, 310)
        blank_label3.show()

        blank_label4 = QLabel('제목', self)
        blank_label4.resize(600, 72)
        blank_label4.setStyleSheet("border: 1px solid #b1ffa7;")
        blank_label4.move(450, 390)
        blank_label4.show()

        blank_label5 = QLabel('제목', self)
        blank_label5.resize(600, 72)
        blank_label5.setStyleSheet("border: 1px solid #b1ffa7;")
        blank_label5.move(450, 470)
        blank_label5.show()

        plus_btn = QPushButton('+플러스', self)
        plus_btn.resize(500, 50)
        plus_btn.setStyleSheet('border: 0;'
                               'display: block;'
                               'font-size: 15px;'
                               'font-weight: bold;'
                               'border-radius: 5px;'
                               'background-color: #5dda72;')
        plus_btn.move(500, 570)
        plus_btn.show()

        modify_btn = QPushButton('수정', self)
        modify_btn.resize(220, 30)
        modify_btn.setStyleSheet("background-color: #94ff85;"
                                 "border-radius: 10px;"
                                 "color: #00791e;"
                                 )
        modify_btn.move(105, 575)
        modify_btn.show()

        modify_btn2_1 = QLabel('수정', self)
        modify_btn2_1.resize(120, 70)
        modify_btn2_1.setStyleSheet("border-radius : 5px;"
                                    "background-color: #b1ffa7;")
        modify_btn2_1.setAlignment(Qt.AlignCenter)
        modify_btn2_1.move(1100, 150)
        modify_btn2_1.show()

        modify_btn2_2 = QLabel('수정', self)
        modify_btn2_2.resize(120, 70)
        modify_btn2_2.setStyleSheet("border-radius : 5px;"
                                    "background-color: #b1ffa7;")
        modify_btn2_2.setAlignment(Qt.AlignCenter)
        modify_btn2_2.move(1100, 230)
        modify_btn2_2.show()

        modify_btn2_3 = QLabel('수정', self)
        modify_btn2_3.resize(120, 70)
        modify_btn2_3.setStyleSheet("border-radius : 5px;"
                                    "background-color: #b1ffa7;")
        modify_btn2_3.setAlignment(Qt.AlignCenter)
        modify_btn2_3.move(1100, 310)
        modify_btn2_3.show()

        modify_btn2_4 = QLabel('수정', self)
        modify_btn2_4.resize(120, 70)
        modify_btn2_4.setStyleSheet("border-radius : 5px;"
                                    "background-color: #b1ffa7;")
        modify_btn2_4.setAlignment(Qt.AlignCenter)
        modify_btn2_4.move(1100, 390)
        modify_btn2_4.show()

        modify_btn2_5 = QLabel('수정', self)
        modify_btn2_5.resize(120, 70)
        modify_btn2_5.setStyleSheet("border-radius : 5px;"
                                    "background-color: #b1ffa7;")
        modify_btn2_5.setAlignment(Qt.AlignCenter)
        modify_btn2_5.move(1100, 470)
        modify_btn2_5.show()

    def func_close(self):
        self.close()

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

        self.label_main = QLabel('LOGIN', self)
        self.label_main.move(100, 50)

        self.label_image = QLabel(self)

        #QLabel design 설정
        label_background.setStyleSheet("background-color: #7a978d")
        self.label_main.setStyleSheet("font: 70px MS PGothic;")


        #QLineEdit 선언 및 기본적인 설정
        self.LineEdit_id = QLineEdit(self)
        self.LineEdit_pw = QLineEdit(self)

        self.LineEdit_id.resize(330, 50)
        self.LineEdit_id.move(35, 170)
        self.LineEdit_id.setPlaceholderText("ID")

        self.LineEdit_pw.resize(330, 50)
        self.LineEdit_pw.move(35, 240)
        self.LineEdit_pw.setPlaceholderText('Password')
        self.LineEdit_pw.setEchoMode(QLineEdit.Password)

        #QLineEdit design 설정
        self.LineEdit_id.setStyleSheet("border-radius: 15px;"
                                       "font: 17px;"
                                       "font-weight: bold;")

        self.LineEdit_pw.setStyleSheet("border-radius: 15px;"
                                       "font: 17px;"
                                       "font-weight: bold;")

        #QPushButton 선언 및 기본 설정
        self.Button_login = QPushButton('login', self)
        self.Button_login.resize(200, 50)
        self.Button_login.move(95, 330)
        self.Button_login.clicked.connect(self.func_close_id)

        self.Button_new = QPushButton('회원가입', self)
        self.Button_new.move(154, 400)
        self.Button_new.clicked.connect(self.Click_new)

        #QPushButton design 설정
        self.Button_login.setStyleSheet("QPushButton:hover{border-radius: 15px; background-color: #C9CFCD;}"
                                        "QPushButton{border-radius: 15px; background-color: #DDDDDD; font: 25px; font-weight: bold;}")
        self.Button_new.setStyleSheet("color: #37573B; background-color: #7a978d; border-width: 1px; border-style: solid;border-color: #7a978d #7a978d #37573B #7a978d;"
                                      "font: 20px; font-weight: bold;")

        #QPixmap 선언 및 기본 설정
        self.pixmap_color = QPixmap('img/ReQuiz_logo_black.png')
        self.pixmap_color = self.pixmap_color.scaledToHeight(150)
        self.label_image.move(123, 405)
        self.label_image.setPixmap(self.pixmap_color)

    def func_close_id(self):
        self.close()
        QMessageBox.about(self, "Login", "Login Successful!")

    def Click_new(self):
        self.label_main.close()
        self.label_image.close()
        self.LineEdit_pw.close()
        self.LineEdit_id.close()
        self.Button_login.close()
        self.Button_new.close()

        self.unitUI_new()

    def unitUI_new(self):
        self.setWindowTitle('Sign up')
        # QLabel 선언 및 기본적인 설정
        label_main = QLabel('SIGN UP', self)
        label_main.move(105, 30)

        # QLabel design 설정
        label_main.setStyleSheet("font: 50px MS PGothic; color: white;")
        label_main.show()

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
        LineEdit_name.show()
        LineEdit_pw_chek.show()
        LineEdit_pw.show()
        LineEdit_id.show()

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

        Button_check_name.show()
        Button_check_id.show()
        Button_new.show()

    def func_close(self):
        self.close()
        QMessageBox.about(self, "Sign up", "Sign up Successful!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = Main_Window()
    sys.exit(app.exec_())