import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *


class Main_Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI_main()
        self.setWindowIcon(QIcon('img/ReQuiz_logo_color.png'))
        self.setWindowTitle('Requiz')
        self.setFixedSize(1300, 800)
        self.show()

    def initUI_main(self):
        # label 선언 및 기본적인 설정
        line = QLabel('', self)
        line.move(0, 120)
        line.resize(1300, 680)

        self.label_main = QLabel('REQUIZ', self)
        self.label_main.move(450, 230)

        label_logo = QLabel('', self)
        label_logo.resize(1300, 120)
        label_logo.setAlignment(Qt.AlignCenter)

        label_picture_header = QLabel(self)
        label_picture_white = QLabel(self)

        # label design 설정
        line.setStyleSheet("background-image: url(img/ReQuiz_background_image.png);")

        label_logo.setStyleSheet("background: linear-gradient(to right, #139dba , #397fb3);"
                                 "color : white;")
        self.label_main.setStyleSheet("color : white;"
                                      "font:65pt Segoe UI Black;")

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
        pixmap_header = QPixmap('img/ReQuiz_header_image.png')
        pixmap_header = pixmap_header.scaledToHeight(120)
        label_picture_header.move(-500, 0)
        label_picture_header.setPixmap(pixmap_header)

        pixmap_white = QPixmap('img/ReQuiz_logo_white.png')
        pixmap_white = pixmap_white.scaledToHeight(150)
        label_picture_white.move(570, -15)
        label_picture_white.setPixmap(pixmap_white)

        # QLineEdit 선언 및 기본적인 설정
        self.LineEdit_search_id = QLineEdit(self)
        self.LineEdit_search_id.resize(560, 60)
        self.LineEdit_search_id.move(370, 420)

        # QLineEdit design 설정
        self.LineEdit_search_id.setPlaceholderText('Please enter the ID to search')
        self.LineEdit_search_id.setStyleSheet("border: 1px solid #ffaef8;"
                                              "border-radius: 10px;"
                                              "font: 25px Bahnschrift")

        # button 선언 및 기본적인 설정
        self.button_search_id = QPushButton('Search', self)
        self.button_login = QPushButton("로그인", self)
        self.button_logout = QPushButton('로그아웃', self)

        self.button_search_id.resize(560, 50)
        self.button_search_id.move(370, 500)
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

        self.button_search_id.setStyleSheet(
            "QPushButton:hover{background-color: #A5E6E4; border-radius: 15px; font: Bahnschrift; font-weight: bold; color: black}"
            "QPushButton{background-color: #ade9e7;"
            "font: Bahnschrift;" 
            "font-weight: bold;"
            "border-radius: 15px;"
            "color: black;}")

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

        self.profile_pix = QPixmap('img/200x200.png')
        self.profile_label = QLabel(self)
        self.profile_label.move(115, 200)
        self.profile_label.setPixmap(self.profile_pix)
        self.profile_label.show()

        self.label_myid = QLabel('Id: ', self)
        self.label_myid.setStyleSheet('border:1px solid; border-color: #6FA893 #6FA893 #968383  #6FA893; font: 30px Bahnschrift;')
        self.label_myid.move(95, 440)
        self.label_myid.resize(240, 40)
        self.label_myid.show()

        self.label_myname = QLabel('Name: ', self)
        self.label_myname.setStyleSheet('border:1px solid; border-color: #6FA893 #6FA893 #968383  #6FA893; font: 30px Bahnschrift;')
        self.label_myname.move(95, 500)
        self.label_myname.resize(240, 40)
        self.label_myname.show()


        self.plus_btn = QPushButton('+', self)
        self.plus_btn.clicked.connect(self.click_plus)
        self.plus_btn.resize(750, 50)
        self.plus_btn.setStyleSheet('QPushButton{border: 0;'
                                    'display: block;'
                                    'font-size: 50px;'
                                    'border-radius: 10px;'
                                    'background-color: #6A83CF;}'
                                    'QPushButton:hover{border: 0;'
                                    'display: block;'
                                    'font-size: 50px;'
                                    'border-radius: 10px;'
                                    'background-color: #596ac9;}')
        self.plus_btn.move(450, 300)
        self.plus_btn.show()

        self.modify_btn = QPushButton('회원정보 수정', self)
        self.modify_btn.resize(260, 35)
        self.modify_btn.setStyleSheet("QPushButton:hover{background-color: #6A83CF;border_radius: 10px;color: white;}"
                                      "QPushButton{background-color: #596ac9; border-radius: 10px; color: white;}")
        self.modify_btn.move(87, 570)
        self.modify_btn.show()

        self.button_library = QPushButton('First Library', self)
        self.button_library.resize(600, 72)
        self.button_library.setStyleSheet("QPushButton{background-color: white; border-radius: 10px; font: 30px Bahnschrift;}"
                                          "QPushButton:hover{background-color: #cccccc; border-radius: 10px; font: 30px Bahnschrift;}")
        self.button_library.move(450, 200)
        self.button_library.show()
        self.button_library.clicked.connect(self.click_word)

        self.modify_btn2 = QPushButton('수정', self)
        self.modify_btn2.resize(120, 70)
        self.modify_btn2.setStyleSheet("QPushButton{background-color: #596ac9; border-radius: 5px; color: white;}"
                                       "QPushButton:hover{background-color: #6A83CF; border-radius: 5px; color: white;}")
        self.modify_btn2.move(1070, 200)
        self.modify_btn2.show()

    def click_plus(self):
        self.profile_label.close()
        self.label_myid.close()
        self.label_myname.close()
        self.button_library.close()
        self.plus_btn.close()
        self.modify_btn.close()
        self.modify_btn2.close()

        self.initUI_write()

    def initUI_write(self):
        self.setWindowTitle('Write')

        # QLineEdit 선언 및 기본 설정
        self.LineEdit_dict_title = QLineEdit(self)
        self.LineEdit_dict_question1 = QLineEdit(self)
        self.LineEdit_dict_answer1 = QLineEdit(self)

        self.LineEdit_dict_title.resize(600, 50)
        self.LineEdit_dict_title.move(300, 155)
        self.LineEdit_dict_title.setPlaceholderText("Please enter a workbook title")
        self.LineEdit_dict_title.setAlignment(Qt.AlignCenter)

        self.LineEdit_dict_question1.resize(800, 50)
        self.LineEdit_dict_question1.move(300, 240)
        self.LineEdit_dict_question1.setPlaceholderText('Please enter a question')

        self.LineEdit_dict_answer1.resize(800, 50)
        self.LineEdit_dict_answer1.move(300, 290)
        self.LineEdit_dict_answer1.setPlaceholderText('Please enter a answer')

        # QLineEdit design 설정
        self.LineEdit_dict_title.setStyleSheet('''
                                               border-radius: 10px;
                                               font: 40px Bahnschrift;
                                               ''')
        self.LineEdit_dict_question1.setStyleSheet('''
                                                   border-top-right-radius: 10px;
                                                   border: 1px solid #686869;
                                                   padding-left: 10px;
                                                   font: 25px Bahnschrift;
                                                   font-weight: bold; 
                                                   ''')
        self.LineEdit_dict_answer1.setStyleSheet('''
                                                 border-bottom-right-radius: 10px;
                                                 border: 1px solid #686869;
                                                 padding-left: 10px;
                                                 font: 25px Bahnschrift;
                                                 ''')
        self.LineEdit_dict_title.show()
        self.LineEdit_dict_question1.show()
        self.LineEdit_dict_answer1.show()

        # QLabel 선언 및 기본 선언
        self.label_th_1 = QLabel('1', self)
        self.label_th_1.show()
        self.label_th_1.resize(120, 100)
        self.label_th_1.move(180, 240)
        self.label_th_1.setAlignment(Qt.AlignCenter)

        # QLabel design 설정
        self.label_th_1.setStyleSheet('''
                                      background-color: #648277;
                                      color: white;
                                      font: 60px Bahnschrift;
                                      font-weight: bold;
                                      border-top-left-radius: 10px;
                                      border-bottom-left-radius: 10px;
                                      ''')
        self.label_th_1.show()

        # QpushButton 선언 및 기본적인 설정
        self.button_plus_word = QPushButton('+', self)
        self.button_plus_word.resize(800, 50)
        self.button_plus_word.move(250, 400)

        self.button_create = QPushButton('Create', self)
        self.button_create.resize(120, 60)
        self.button_create.move(960, 150)

        # QPushButton design 설정
        self.button_plus_word.setStyleSheet('''
                                            QPushButton:hover{border-radius: 10px; background-color: #668A7D;color: white; font: 65px; font-weight: bold;}
                                            QPushButton{border-radius: 10px; background-color: #648277;color: white; font: 65px; font-weight: bold;}
                                            ''')
        self.button_create.setStyleSheet('''
                                        QPushButton:hover{border-radius: 10px; background-color: #668A7D;color: white; font: 25px Bahnschrift;}
                                        QPushButton{border-radius: 10px; background-color: #648277;color: white; font: 25px Bahnschrift;}
                                        ''')
        self.button_plus_word.show()
        self.button_create.show()

    def click_word(self):
        self.profile_label.close()
        self.label_myid.close()
        self.label_myname.close()
        self.plus_btn.close()
        self.modify_btn.close()
        self.modify_btn2.close()
        self.button_library.close()

        self.initUI_word()

    def initUI_word(self):
        self.setWindowTitle('Library')

        # label design 설정
        self.label_question1 = QLabel('● Requin은 무엇일까요?\t\t\t\t\t\t\t\t\t', self)
        self.label_question1.move(200, 200)

        self.label_question1.setStyleSheet("color: black;"
                                 "background-color: #FFFFFF;"
                                 "border-style: soild;"
                                 "border-width: 25px;"
                                 "font-weight: bold;")
        self.label_question1.show()


        self.label_answer1 = QLabel('\t▶ Requin은 대덕소프트웨어마이스터고등학교 5기 학생들이 만든 팀입니다!\t\t\t\t', self)
        self.label_answer1.move(200, 300)
        self.label_answer1.setStyleSheet("color: black;"
                                 "background-color: #FFFFFF;"
                                 "border-style: soild;"
                                 "border-width: 25px;"
                                 "font-weight: bold;")

        self.label_answer1.show()

        self.button_more = QPushButton('더보기', self)
        self.button_more.resize(500, 50)
        self.button_more.move(400, 700)
        self.button_more.setStyleSheet("QPushButton:hover{border-radius: 10px; background-color: #2F9D27;}"
                              "QPushButton{border-radius: 10px; background-color: #22741C; font: 15px; color: white;"
                              "font-weight: bold;}")
        self.button_more.show()

        self.label_picture_white = QLabel(self)
        pixmap_white = QPixmap('img/requin_white.png')
        pixmap_white = pixmap_white.scaledToHeight(150)
        self.label_picture_white.move(570, -15)
        self.label_picture_white.setPixmap(pixmap_white)
        self.label_picture_white.show()

    def func_signup(self):
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
        # QLabel 선언 및 기본적인 설정
        label_background = QLabel('', self)
        label_background.resize(400, 550)

        self.label_main = QLabel('LOGIN', self)
        self.label_main.move(100, 50)

        self.label_image = QLabel(self)

        # QLabel design 설정
        label_background.setStyleSheet("background-color: #ade9e7")
        self.label_main.setStyleSheet("color: white; font: 70px MS PGothic;")

        # QLineEdit 선언 및 기본적인 설정
        self.LineEdit_id = QLineEdit(self)
        self.LineEdit_pw = QLineEdit(self)

        self.LineEdit_id.resize(330, 50)
        self.LineEdit_id.move(35, 170)
        self.LineEdit_id.setPlaceholderText("ID")

        self.LineEdit_pw.resize(330, 50)
        self.LineEdit_pw.move(35, 240)
        self.LineEdit_pw.setPlaceholderText('Password')
        self.LineEdit_pw.setEchoMode(QLineEdit.Password)

        # QLineEdit design 설정
        self.LineEdit_id.setStyleSheet("border-radius: 15px;"
                                       "font: 17px;"
                                       "font-weight: bold;")

        self.LineEdit_pw.setStyleSheet("border-radius: 15px;"
                                       "font: 17px;"
                                       "font-weight: bold;")

        # QPushButton 선언 및 기본 설정
        self.Button_login = QPushButton('login', self)
        self.Button_login.resize(200, 50)
        self.Button_login.move(95, 330)
        self.Button_login.clicked.connect(self.func_login)

        self.Button_new = QPushButton('회원가입', self)
        self.Button_new.move(154, 400)
        self.Button_new.clicked.connect(self.Click_new)

        # QPushButton design 설정
        self.Button_login.setStyleSheet("QPushButton:hover{border-radius: 15px; background-color: #C9CFCD;}"
                                        "QPushButton{border-radius: 15px; background-color: #DDDDDD; font: 25px; font-weight: bold;}")
        self.Button_new.setStyleSheet(
            "color: white; background-color: #ade9e7; border: 0px;"
            "font: 20px; font-weight: bold;")

        # QPixmap 선언 및 기본 설정
        self.pixmap_color = QPixmap('img/ReQuiz_logo_black.png')
        self.pixmap_color = self.pixmap_color.scaledToHeight(150)
        self.label_image.move(123, 405)
        self.label_image.setPixmap(self.pixmap_color)

    def func_login(self):
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
        Button_new.clicked.connect(self.func_signup)

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
            "QPushButton:hover{border-radius: 5px; background-color: #6A83CF; font: 15px; color: white; font-weight: bold;}"
            "QPushButton{border-radius: 5px; background-color: #596ac9; font: 15px; color: white; font-weight: bold;}")
        Button_check_id.setStyleSheet(
            "QPushButton:hover{border-radius: 5px; background-color: #6A83CF; font: 15px; color: white; font-weight: bold;}"
            "QPushButton{border-radius: 5px; background-color: #596ac9; font: 15px; color: white; font-weight: bold;}")

        Button_check_name.show()
        Button_check_id.show()
        Button_new.show()

    def func_signup(self):
        self.close()
        QMessageBox.about(self, "Sign up", "Sign up Successful!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = Main_Window()
    sys.exit(app.exec_())