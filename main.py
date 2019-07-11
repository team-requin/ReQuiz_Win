import sys
import requests, json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *


class Main_Window(QWidget):
    gap_in_write = 1
    def __init__(self):
        super().__init__()
        self.initUI_main()
        self.setWindowIcon(QIcon('img/ReQuiz_logo_color.png'))
        self.setFixedSize(1300, 800)
        self.show()

    def initUI_main(self):
        self.setWindowTitle('Requiz')

        # label 선언 및 기본적인 설정
        self.line = QLabel('', self)
        self.line.move(0, 120)
        self.line.resize(1300, 680)
        self.line.setStyleSheet("background-image: url(img/ReQuiz_background_image.png);")
        self.line.show()

        self.label_main = QLabel('REQUIZ', self)
        self.label_main.move(450, 230)

        label_logo = QLabel('', self)
        label_logo.resize(1300, 120)
        label_logo.setAlignment(Qt.AlignCenter)

        label_picture_header = QLabel(self)
        label_picture_white = QLabel(self)

        # label design 설정
        label_logo.setStyleSheet("color : white;")
        self.label_main.setStyleSheet("color : white;"
                                      "font:65pt Segoe UI Black;")
        self.label_main.show()

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
        self.LineEdit_search_id.show()

        # button 선언 및 기본적인 설정
        self.button_search_id = QPushButton('Search', self)
        self.button_login = QPushButton("Log in", self)
        self.button_logout = QPushButton('Log out', self)

        self.button_search_id.resize(560, 50)
        self.button_search_id.move(370, 500)
        self.button_search_id.clicked.connect(self.click_search)

        self.button_login.resize(100, 50)
        self.button_login.move(1050, 35)
        self.button_login.clicked.connect(self.onClick_login)

        self.button_logout.resize(100, 50)
        self.button_logout.move(1170, 35)

        # button design 설정
        self.button_login.setStyleSheet("QPushButton:hover{background:qradialgradient(cx:1.5, cy:1.0, radius: 2.5, fx:1.5, fy:1.0, stop:0 white, stop:1 #87ff87); "
                                        "border-radius: 15px;  font-weight: bold; font: 22px Bahnschrift; "
                                        "color: black;}"
                                        "QPushButton{background-color: #C1FFC1;"
                                        "border-radius: 15px;"
                                        "font-weight: bold;"
                                        "font: 22px Bahnschrift;"
                                        "color: black;}")

        self.button_logout.setStyleSheet("QPushButton:hover{background:qradialgradient(cx:1.5, cy:1.0, radius: 2.5, fx:1.5, fy:1.0, stop:0 white, stop:1 #87ff87); "
                                         "border-radius: 15px;  font-weight: bold; font: 22px Bahnschrift; "
                                         "color: black;}"
                                         "QPushButton{background-color: #C1FFC1;"
                                         "border-radius: 15px;"
                                         "font-weight: bold;"
                                         "font: 22px Bahnschrift;"
                                         "color: black;}")

        self.button_search_id.setStyleSheet(
            "QPushButton:hover{border:1px solid #7497CF; background-color: #A5E6E4; border-radius: 15px; font: Bahnschrift; font-weight: bold; color: black}"
            "QPushButton{background-color: #ade9e7;"
            "border:1px solid #7497CF;"
            "font: Bahnschrift;"
            "font-weight: bold;"
            "border-radius: 15px;"
            "color: black;}")
        self.button_login.show()
        self.button_logout.show()
        self.button_search_id.show()

    def onClick_login(self):
        self.main_to_login = Login_Window()

    def click_search(self):
        self.button_search_id.close()
        self.button_login.close()
        self.LineEdit_search_id.close()
        self.button_logout.close()
        self.label_main.close()
        self.line.close()

        self.initUI_list()

    def initUI_list(self):
        self.setWindowTitle('List')

        self.line = QLabel('', self)
        self.line.move(0, 120)
        self.line.resize(1300, 680)
        self.line.setStyleSheet("background-image: url(img/ReQuiz_background2_image.png);")
        self.line.show()

        self.profile_pix = QPixmap('img/200x200.png')
        self.profile_label = QLabel(self)
        self.profile_label.move(115, 200)
        self.profile_label.setPixmap(self.profile_pix)
        self.profile_label.show()

        self.label_myid = QLabel('Id: ', self)
        self.label_myid.setStyleSheet('border:1px solid; border-width: 0px 0px 1px 0px; border-color: #6FA893 #6FA893 #968383  #6FA893; font: 30px Bahnschrift;')
        self.label_myid.move(95, 440)
        self.label_myid.resize(240, 40)
        self.label_myid.show()

        self.label_myname = QLabel('Name: ', self)
        self.label_myname.setStyleSheet('border:solid; border-width: 0px 0px 1px 0px; border-color: #6FA893 #6FA893 #968383  #6FA893; font: 30px Bahnschrift;')
        self.label_myname.move(95, 500)
        self.label_myname.resize(240, 40)
        self.label_myname.show()

        self.back_btn = QPushButton('←', self)
        self.back_btn.resize(120, 70)
        self.back_btn.move(70, 27)
        self.back_btn.setStyleSheet("QPushButton:hover{background:qradialgradient(cx:1.5, cy:1.0, radius: 2.5, fx:1.5, fy:1.0, stop:0 white, stop:1 #87ff87); border-radius: 10px;"
                                    "font: 80px; font-weight: bold}"
                                    "QPushButton{background-color: #C1FFC1; border-radius: 10px; font: 80px; font-weight: bold}")
        self.back_btn.clicked.connect(self.click_back_in_list)
        self.back_btn.show()

        self.plus_btn = QPushButton('+', self)
        self.plus_btn.clicked.connect(self.click_write)
        self.plus_btn.resize(60, 60)
        self.plus_btn.setStyleSheet('QPushButton{'
                                    'display: block;'
                                    'font-size: 50px;'
                                    'color: white;'
                                    'border-radius: 30px;'
                                    'background-color: #FEBC01;}'
                                    'QPushButton:hover{;'
                                    'display: block;'
                                    'border-radius: 30px;'
                                    'font-size: 50px;'
                                    'background-color: #f0cd35;}')
        self.plus_btn.move(720, 290)
        self.plus_btn.show()

        self.modify_btn = QPushButton('Modify information', self)
        self.modify_btn.resize(260, 35)
        self.modify_btn.setStyleSheet("QPushButton:hover{background-color: #6A83CF;border_radius: 10px;color: white;}"
                                      "QPushButton{background-color: #596ac9; font: 17px; font-weight: bold; border-radius: 10px; color: white;}")
        self.modify_btn.move(87, 570)
        self.modify_btn.clicked.connect(self.click_modify_information)
        self.modify_btn.show()

        self.button_library = QPushButton('First Library', self)
        self.button_library.resize(600, 60)
        self.button_library.setStyleSheet("QPushButton{background-color: white; border-radius: 30px; font: 30px Bahnschrift;}"
                                          "QPushButton:hover{background-color: #cccccc; border-radius: 30px; font: 30px Bahnschrift;}")
        self.button_library.move(450, 200)
        self.button_library.show()
        self.button_library.clicked.connect(self.click_word)

        self.modify_btn2 = QPushButton('Modify', self)
        self.modify_btn2.resize(90, 60)
        self.modify_btn2.setStyleSheet("QPushButton{background-color: #596ac9; border-radius: 30px; color: white; font: 20px Bahnschrift; font-weight: bold;}"
                                       "QPushButton:hover{background-color: #6A83CF; border-radius: 30px; color: white;}")
        self.modify_btn2.move(980, 200)
        self.modify_btn2.clicked.connect(self.click_modify_word)
        self.modify_btn2.show()

    def click_back_in_list(self):
        self.profile_label.close()
        self.label_myid.close()
        self.label_myname.close()
        self.button_library.close()
        self.plus_btn.close()
        self.modify_btn.close()
        self.modify_btn2.close()
        self.back_btn.close()
        self.line.close()

        self.initUI_main()

    def click_modify_information(self):
        self.profile_label.close()
        self.label_myid.close()
        self.label_myname.close()
        self.button_library.close()
        self.plus_btn.close()
        self.modify_btn.close()
        self.modify_btn2.close()
        self.back_btn.close()

        self.initUI_modify_information()

    def initUI_modify_information(self):
        #QLabel 설정

        self.label_id = QLabel('ID', self)
        self.label_id.move(670, 253)
        self.label_id.setStyleSheet("font: 50px Bahnschrift; font-weight: bold;")
        self.label_id.show()

        self.label_id_value = QLabel('admin', self)
        self.label_id_value.setAlignment(Qt.AlignCenter)
        self.label_id_value.move(850, 260)
        self.label_id_value.resize(330, 50)
        self.label_id_value.setStyleSheet("background-color: white; border-radius: 20px; font: 30px Bahnschrift; font-weight: bold; color: #A3A4A3")
        self.label_id_value.show()

        self.label_id_message = QLabel('아이디는 변경이 불가능합니다.', self)
        self.label_id_message.move(905, 320)
        self.label_id_message.setStyleSheet("font-weight: bold;")
        self.label_id_message.show()

        self.label_nickname = QLabel('NICKNAME', self)
        self.label_nickname.move(590, 350)
        self.label_nickname.setStyleSheet("font: 50px Bahnschrift; font-weight: bold;")
        self.label_nickname.show()

        self.LineEdit_nickname_value = QLineEdit('admin', self)
        self.LineEdit_nickname_value.setAlignment(Qt.AlignCenter)
        self.LineEdit_nickname_value.move(850, 360)
        self.LineEdit_nickname_value.resize(330, 50)
        self.LineEdit_nickname_value.setStyleSheet("background-color: white; border-radius: 20px; font: 30px Bahnschrift; font-weight: bold; color: black;")
        self.LineEdit_nickname_value.show()

        self.label_pw = QLabel('PW', self)
        self.label_pw.move(660, 445)
        self.label_pw.setStyleSheet("font: 50px Bahnschrift; font-weight: bold;")
        self.label_pw.show()

        self.LineEdit_pw_value = QLineEdit('', self)
        self.LineEdit_pw_value.setAlignment(Qt.AlignCenter)
        self.LineEdit_pw_value.move(850, 450)
        self.LineEdit_pw_value.resize(330, 50)
        self.LineEdit_pw_value.setStyleSheet(
            "background-color: white; border-radius: 20px; font: 30px Bahnschrift; font-weight: bold; color: black;")
        self.LineEdit_pw_value.show()

        self.label_pw_check = QLabel('PW check', self)
        self.label_pw_check.move(600, 530)
        self.label_pw_check.setStyleSheet("font: 50px Bahnschrift; font-weight: bold;")
        self.label_pw_check.show()

        self.LineEdit_pw_check_value = QLineEdit('', self)
        self.LineEdit_pw_check_value.setAlignment(Qt.AlignCenter)
        self.LineEdit_pw_check_value.move(850, 540)
        self.LineEdit_pw_check_value.resize(330, 50)
        self.LineEdit_pw_check_value.setStyleSheet("background-color: white; border-radius: 20px; font: 30px Bahnschrift; font-weight: bold; color: black;")
        self.LineEdit_pw_check_value.show()

        self.label_picture = QLabel('', self)
        self.label_picture.resize(340, 340)
        self.label_picture.move(150, 260)
        self.label_picture.setStyleSheet("background-color: white; border-radius: 20px;")
        self.label_picture.show()

        #QPushButton 설정

        self.button_modify_complete = QPushButton('Complete', self)
        self.button_modify_complete.move(550, 670)
        self.button_modify_complete.resize(200, 50)
        self.button_modify_complete.setStyleSheet("QPushButton{font: 30px Bahnschrift; color: white; border-radius: 10px; background-color: #6BA4E8;}"
                                                  "QPushButton:hover{font: 30px Bahnschrift; color: white; border-radius: 10px; background-color: #85b3ff;}")
        self.button_modify_complete.clicked.connect(self.button_modify_complete_click)
        self.button_modify_complete.show()

        self.back_btn = QPushButton('←', self)
        self.back_btn.resize(120, 70)
        self.back_btn.move(70, 27)
        self.back_btn.clicked.connect(self.click_back_in_modify)
        self.back_btn.setStyleSheet(
            "QPushButton:hover{background:qradialgradient(cx:1.5, cy:1.0, radius: 2.5, fx:1.5, fy:1.0, stop:0 white, stop:1 #87ff87); border-radius: 10px;"
            "font: 80px; font-weight: bold}"
            "QPushButton{background-color: #C1FFC1; border-radius: 10px; font: 80px; font-weight: bold}")
        self.back_btn.show()

    def click_modify_word(self):
        self.profile_label.close()
        self.label_myid.close()
        self.label_myname.close()
        self.button_library.close()
        self.plus_btn.close()
        self.modify_btn.close()
        self.modify_btn2.close()
        self.back_btn.close()

        self.initUI_modify_word()

    def initUI_modify_word(self):
        self.setWindowTitle('Modify')

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
                                                           border: 1px solid #596ac9;
                                                           padding-left: 10px;
                                                           font: 25px Bahnschrift;
                                                           ''')
        self.LineEdit_dict_answer1.setStyleSheet('''
                                                         border-bottom-right-radius: 10px;
                                                         border: 1px solid #596ac9;
                                                         padding-left: 10px;
                                                         font: 20px Bahnschrift;
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
                                              background-color: #596ac9;
                                              color: white;
                                              font: 60px Bahnschrift;
                                              font-weight: bold;
                                              border-top-left-radius: 10px;
                                              border-bottom-left-radius: 10px;
                                              ''')
        self.label_th_1.show()

        # QpushButton 선언 및 기본적인 설정
        self.button_plus_word = QPushButton('More', self)
        self.button_plus_word.resize(800, 50)
        self.button_plus_word.move(250, 400)

        self.button_create = QPushButton('Modify', self)
        self.button_create.resize(120, 60)
        self.button_create.move(960, 150)
        self.button_create.clicked.connect(self.click_create_list)

        self.back_btn = QPushButton('←', self)
        self.back_btn.resize(120, 70)
        self.back_btn.move(70, 27)
        self.back_btn.clicked.connect(self.click_back_in_write)
        self.back_btn.setStyleSheet(
            "QPushButton:hover{background:qradialgradient(cx:1.5, cy:1.0, radius: 2.5, fx:1.5, fy:1.0, stop:0 white, stop:1 #87ff87); border-radius: 10px;"
            "font: 80px; font-weight: bold}"
            "QPushButton{background-color: #C1FFC1; border-radius: 10px; font: 80px; font-weight: bold}")
        self.back_btn.show()

        # QPushButton design 설정
        self.button_plus_word.setStyleSheet('''
                                                    QPushButton:hover{border-radius: 10px; background-color: #6A83CF;color: white; font: 30px; font-weight: bold;}
                                                    QPushButton{border-radius: 10px; background-color: #596ac9;color: white; font: 30px; font-weight: bold;}
                                                    ''')
        self.button_create.setStyleSheet('''
                                                QPushButton:hover{border-radius: 10px; background-color: #6A83CF;color: white; font: 25px Bahnschrift;}
                                                QPushButton{border-radius: 10px; background-color: #596ac9;color: white; font: 25px Bahnschrift;}
                                                ''')

        self.button_plus_word.show()
        self.button_create.show()

    def button_modify_complete_click(self):
        QMessageBox.about(self, "message", "Modify successful!!")
        self.label_id.close()
        self.label_nickname.close()
        self.label_pw.close()
        self.label_pw_check.close()
        self.label_picture.close()
        self.label_id_value.close()
        self.LineEdit_nickname_value.close()
        self.LineEdit_pw_value.close()
        self.LineEdit_pw_check_value.close()
        self.button_modify_complete.close()
        self.back_btn.close()
        self.label_id_message.close()

        self.initUI_list()

    def click_back_in_modify(self):
        self.label_id.close()
        self.label_nickname.close()
        self.label_pw.close()
        self.label_pw_check.close()
        self.label_picture.close()
        self.label_id_value.close()
        self.LineEdit_nickname_value.close()
        self.LineEdit_pw_value.close()
        self.LineEdit_pw_check_value.close()
        self.button_modify_complete.close()
        self.back_btn.close()
        self.label_id_message.close()

        self.initUI_list()

    def click_write(self):
        self.profile_label.close()
        self.label_myid.close()
        self.label_myname.close()
        self.button_library.close()
        self.plus_btn.close()
        self.modify_btn.close()
        self.modify_btn2.close()
        self.back_btn.close()

        self.initUI_write()

    def initUI_write(self):
        self.setWindowTitle('Write')
        Main_Window.gap_in_write = 0

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
                                                   border: 1px solid #596ac9;
                                                   padding-left: 10px;
                                                   font: 25px Bahnschrift;
                                                   ''')
        self.LineEdit_dict_answer1.setStyleSheet('''
                                                 border-bottom-right-radius: 10px;
                                                 border: 1px solid #596ac9;
                                                 padding-left: 10px;
                                                 font: 20px Bahnschrift;
                                                 ''')
        self.LineEdit_dict_title.show()
        self.LineEdit_dict_question1.show()
        self.LineEdit_dict_answer1.show()

        # QLabel 선언 및 기본 선언
        self.label_th_1 = QLabel(str(Main_Window.gap_in_write+1), self)
        self.label_th_1.show()
        self.label_th_1.resize(120, 100)
        self.label_th_1.move(180, 240)
        self.label_th_1.setAlignment(Qt.AlignCenter)

        # QLabel design 설정
        self.label_th_1.setStyleSheet('''
                                      background-color: #596ac9;
                                      color: white;
                                      font: 60px Bahnschrift;
                                      font-weight: bold;
                                      border-top-left-radius: 10px;
                                      border-bottom-left-radius: 10px;
                                      ''')
        self.label_th_1.show()

        # QpushButton 선언 및 기본적인 설정
        self.button_plus_word = QPushButton('More', self)
        self.button_plus_word.resize(800, 50)
        self.button_plus_word.move(250, 400)
        self.button_plus_word.clicked.connect(self.func_add_word)

        self.button_create = QPushButton('Create', self)
        self.button_create.resize(120, 60)
        self.button_create.move(960, 150)
        self.button_create.clicked.connect(self.click_create_list)

        self.back_btn = QPushButton('←', self)
        self.back_btn.resize(120, 70)
        self.back_btn.move(70, 27)
        self.back_btn.clicked.connect(self.click_back_in_write)
        self.back_btn.setStyleSheet(
            "QPushButton:hover{background:qradialgradient(cx:1.5, cy:1.0, radius: 2.5, fx:1.5, fy:1.0, stop:0 white, stop:1 #87ff87); border-radius: 10px;"
            "font: 80px; font-weight: bold}"
            "QPushButton{background-color: #C1FFC1; border-radius: 10px; font: 80px; font-weight: bold}")
        self.back_btn.show()

        # QPushButton design 설정
        self.button_plus_word.setStyleSheet('''
                                            QPushButton:hover{border-radius: 10px; background-color: #6A83CF;color: white; font: 30px; font-weight: bold;}
                                            QPushButton{border-radius: 10px; background-color: #596ac9;color: white; font: 30px; font-weight: bold;}
                                            ''')
        self.button_create.setStyleSheet('''
                                        QPushButton:hover{border-radius: 10px; background-color: #6A83CF;color: white; font: 25px Bahnschrift;}
                                        QPushButton{border-radius: 10px; background-color: #596ac9;color: white; font: 25px Bahnschrift;}
                                        ''')

        self.button_plus_word.show()
        self.button_create.show()

    def func_add_word(self):
        Main_Window.gap_in_write += 1
        self.LineEdit_dict_question1 = QLineEdit(self)
        self.LineEdit_dict_answer1 = QLineEdit(self)

        self.LineEdit_dict_question1.resize(800, 50)
        self.LineEdit_dict_question1.move(300, 240 + 120*Main_Window.gap_in_write)
        self.LineEdit_dict_question1.setPlaceholderText('Please enter a question')

        self.LineEdit_dict_answer1.resize(800, 50)
        self.LineEdit_dict_answer1.move(300, 290 + 120*Main_Window.gap_in_write)
        self.LineEdit_dict_answer1.setPlaceholderText('Please enter a answer')

        self.label_th_1 = QLabel(str(Main_Window.gap_in_write+1), self)
        self.label_th_1.resize(120, 100)
        self.label_th_1.move(180, 240 + 120*Main_Window.gap_in_write)
        self.label_th_1.setAlignment(Qt.AlignCenter)

        self.LineEdit_dict_question1.setStyleSheet('''
                                                           border-top-right-radius: 10px;
                                                           border: 1px solid #596ac9;
                                                           padding-left: 10px;
                                                           font: 25px Bahnschrift;
                                                           ''')
        self.LineEdit_dict_question1.show()
        self.LineEdit_dict_answer1.setStyleSheet('''
                                                         border-bottom-right-radius: 10px;
                                                         border: 1px solid #596ac9;
                                                         padding-left: 10px;
                                                         font: 20px Bahnschrift;
                                                         ''')
        self.LineEdit_dict_answer1.show()

        # QLabel design 설정
        self.label_th_1.setStyleSheet('''
                                              background-color: #596ac9;
                                              color: white;
                                              font: 60px Bahnschrift;
                                              font-weight: bold;
                                              border-top-left-radius: 10px;
                                              border-bottom-left-radius: 10px;
                                              ''')

        self.button_plus_word.move(250, 400 + 120*Main_Window.gap_in_write)
        self.label_th_1.show()

    def click_create_list(self):
        QMessageBox.about(self, 'Message', 'Complete!!!')

        self.LineEdit_dict_title.close()
        self.LineEdit_dict_answer1.close()
        self.LineEdit_dict_question1.close()
        self.label_th_1.close()
        self.button_plus_word.close()
        self.button_create.close()
        self.back_btn.close()

        self.initUI_list()

    def click_back_in_write(self):
        self.LineEdit_dict_title.close()
        self.LineEdit_dict_answer1.close()
        self.LineEdit_dict_question1.close()
        self.label_th_1.close()
        self.button_plus_word.close()
        self.button_create.close()
        self.back_btn.close()

        self.initUI_list()

    def click_word(self):
        self.profile_label.close()
        self.label_myid.close()
        self.label_myname.close()
        self.plus_btn.close()
        self.modify_btn.close()
        self.modify_btn2.close()
        self.button_library.close()
        self.back_btn.close()
        self.initUI_word()

    def initUI_word(self):
        self.setWindowTitle('Library')

        # label design 설정
        self.label_title = QLabel('Test1', self)
        self.label_title.move(570, 140)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setStyleSheet("font: 70px Bahnschrift;")
        self.label_title.show()

        self.label_question1 = QLabel('●  Requin은 무엇일까요?', self)
        self.label_question1.move(250, 250)
        self.label_question1.resize(800, 45)

        self.label_question1.setStyleSheet("color: black;"
                                           "padding-left: 10px;"
                                           "background-color: #FFFFFF;"
                                           "font: 18px Bahnschrift;"
                                           # "font-weight: bold;"
                                           "border-radius: 20px;")
        self.label_question1.show()


        self.label_answer1 = QLabel('▶ Requin은 대덕소프트웨어마이스터고등학교 5기 학생들이 만든 팀입니다!', self)
        self.label_answer1.move(250, 305)
        self.label_answer1.resize(800, 45)
        self.label_answer1.setStyleSheet("color: black;"
                                         "padding-left: 50px;"
                                         "background-color: #FFFFFF;"
                                         "font: 15px Bahnschrift;"
                                         "border-radius: 20px;")
        self.label_answer1.show()

        self.button_solve = QPushButton('문제 풀러 가기', self)
        self.button_solve.resize(300, 50)
        self.button_solve.move(500, 380)
        self.button_solve.setStyleSheet("QPushButton:hover{border-radius: 20px; background-color: #6A83CF;}"
                                        "QPushButton{border-radius: 20px; background-color: #596ac9; font: 20px Bahnschrift; color: white;"
                                        "font-weight: bold;}")
        self.button_solve.show()
        self.button_solve.clicked.connect(self.click_solve)

        self.back_btn = QPushButton('←', self)
        self.back_btn.resize(120, 70)
        self.back_btn.move(70, 27)
        self.back_btn.setStyleSheet(
            "QPushButton:hover{background:qradialgradient(cx:1.5, cy:1.0, radius: 2.5, fx:1.5, fy:1.0, stop:0 white, stop:1 #87ff87); border-radius: 10px;"
            "font: 80px; font-weight: bold}"
            "QPushButton{background-color: #C1FFC1; border-radius: 10px; font: 80px; font-weight: bold}")
        self.back_btn.clicked.connect(self.click_back_in_word)
        self.back_btn.show()

    def click_back_in_word(self):
        self.label_question1.close()
        self.label_answer1.close()
        self.button_solve.close()
        self.back_btn.close()
        self.label_title.close()

        self.initUI_list()

    def click_solve(self):
        self.label_question1.close()
        self.label_answer1.close()
        self.button_solve.close()
        self.back_btn.close()
        self.label_title.close()

        self.initUI_solve()

    def initUI_solve(self):
        self.setWindowTitle('Solve')

        #QLabel 기본 선언
        self.label_question_inSolve = QLabel('문제 내용', self)
        self.label_question_inSolve.resize(1000, 150)
        self.label_question_inSolve.move(150, 250)
        self.label_question_inSolve.setAlignment(Qt.AlignCenter)
        self.label_question_inSolve.setStyleSheet("padding-left: 60px; font: 70px; font-weight: bold; border: 1px solid black; border-width: 0px 0px 5px 0px")
        self.label_question_inSolve.show()

        self.label_line_bottom = QLabel('', self)
        self.label_line_bottom.resize(1000, 150)
        self.label_line_bottom.move(150, 420)
        self.label_line_bottom.setStyleSheet("border: 1px solid black; border-width: 0px 0px 5px 0px")
        self.label_line_bottom.show()

        self.label_Q = QLabel('Q.', self)
        self.label_Q.move(200, 230)
        self.label_Q.setStyleSheet("font: 150px; font-weight: bold;")
        self.label_Q.show()

        #QLineEdit 기본 선언
        self.LineEdit_answer_inSolve = QLineEdit(self)
        self.LineEdit_answer_inSolve.resize(800, 60)
        self.LineEdit_answer_inSolve.move(250, 450)
        self.LineEdit_answer_inSolve.setAlignment(Qt.AlignCenter)
        self.LineEdit_answer_inSolve.setPlaceholderText('답을 입력해 주세요.')
        self.LineEdit_answer_inSolve.setStyleSheet("padding-left: 50px; font: 40px; border-radius: 15px;")
        self.LineEdit_answer_inSolve.show()

        #QPushButton 기본 선언
        self.button_question_before = QPushButton('Before', self)
        self.button_question_before.resize(130, 60)
        self.button_question_before.move(860, 630)
        self.button_question_before.setStyleSheet(
            "QPushButton:hover{border-radius: 10px; background-color: #6A83CF; font: 20px; color: white; font-weight: bold;}"
            "QPushButton{border-radius: 10px; background-color: #596ac9; font: 20px; color: white; font-weight: bold;}")
        self.button_question_before.show()

        self.button_question_next = QPushButton('Next', self)
        self.button_question_next.resize(130, 60)
        self.button_question_next.move(1000, 630)
        self.button_question_next.setStyleSheet(
            "QPushButton:hover{border-radius: 10px; background-color: #6A83CF; font: 20px; color: white; font-weight: bold;}"
            "QPushButton{border-radius: 10px; background-color: #596ac9; font: 20px; color: white; font-weight: bold;}")
        self.button_question_next.show()

        self.button_question_stop = QPushButton('Stop', self)
        self.button_question_stop.resize(130, 60)
        self.button_question_stop.move(180, 630)
        self.button_question_stop.setStyleSheet(
            "QPushButton:hover{border-radius: 10px; background-color: #6A83CF; font: 20px; color: white; font-weight: bold;}"
            "QPushButton{border-radius: 10px; background-color: #596ac9; font: 20px; color: white; font-weight: bold;}")
        self.button_question_stop.clicked.connect(self.click_question_stop)
        self.button_question_stop.show()

    def click_question_stop(self):
        reply = QMessageBox.question(self, 'Stop', 'Are you sure to stop?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.No:
            return
        self.label_question_inSolve.close()
        self.label_line_bottom.close()
        self.label_Q.close()
        self.LineEdit_answer_inSolve.close()
        self.label_question_inSolve.close()
        self.button_question_before.close()
        self.button_question_stop.close()
        self.button_question_next.close()

        self.initUI_score()

    def initUI_score(self):
        self.setWindowTitle('Score')

        self.setWindowTitle('Score')
        self.label_score_score = QLabel('89', self)
        self.label_score_score.resize(900, 490)
        self.label_score_score.move(200, 230)
        self.label_score_score.setAlignment(Qt.AlignCenter)
        self.label_score_score.setStyleSheet("background-color: white; color: black; font: 250px; font-weight: bold; border-radius: 15px;")
        self.label_score_score.show()

        self.label_score_title = QLabel('Test 단어장', self)
        self.label_score_title.resize(900, 90)
        self.label_score_title.move(200, 170)
        self.label_score_title.setAlignment(Qt.AlignCenter)
        self.label_score_title.setStyleSheet("background-color: #6BA4E8; color: white; font: 50px; font-weight: bold; border-radius: 5px;")
        self.label_score_title.show()

        self.label_score_description = QLabel('당신의 점수는...', self)
        self.label_score_description.move(470, 290)
        self.label_score_description.setStyleSheet("font: 50px; font-weight: bold;")
        self.label_score_description.show()

        self.button_score_back = QPushButton('돌아가기', self)
        self.button_score_back.resize(200, 60)
        self.button_score_back.move(420, 630)
        self.button_score_back.clicked.connect(self.click_score_back)
        self.button_score_back.setStyleSheet('''
                                            QPushButton:hover{border-radius: 10px; background-color: #82b2ff;color: white; font: 30px Bahnschrift; font-weight: bold;}
                                            QPushButton{border-radius: 10px; background-color: #6BA4E8;color: white; font: 30px Bahnschrift; font-weight: bold;}
                                            ''')
        self.button_score_back.show()

        self.button_score_return = QPushButton('다시하기', self)
        self.button_score_return.resize(200, 60)
        self.button_score_return.move(680, 630)
        self.button_score_return.clicked.connect(self.click_score_return)
        self.button_score_return.setStyleSheet('''
                                               QPushButton:hover{border-radius: 10px; background-color: #82b2ff;color: white; font: 30px Bahnschrift; font-weight: bold;}
                                               QPushButton{border-radius: 10px; background-color: #6BA4E8;color: white; font: 30px Bahnschrift; font-weight: bold;}
                                               ''')
        self.button_score_return.show()

    def click_score_back(self):
        self.label_score_description.close()
        self.label_score_title.close()
        self.label_score_score.close()
        self.button_score_back.close()
        self.button_score_return.close()

        self.initUI_list()

    def click_score_return(self):
        self.label_score_description.close()
        self.label_score_title.close()
        self.label_score_score.close()
        self.button_score_back.close()
        self.button_score_return.close()

        self.initUI_word()

    def func_signup(self):
        self.close()


class Login_Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setFixedSize(400, 450)
        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon('img/ReQuiz_logo_color'))
        self.show()

    def initUI(self):
        # QLabel 선언 및 기본적인 설정
        label_background = QLabel('', self)
        label_background.resize(400, 550)

        self.label_main = QLabel('LOGIN', self)
        self.label_main.resize(400, 80)
        self.label_main.setAlignment(Qt.AlignCenter)

        self.label_image = QLabel(self)

        # QLabel design 설정
        label_background.setStyleSheet("background-color: #f8f8f8")
        self.label_main.setStyleSheet("color: white; font: 50px MS PGothic; background-color: #187aca;")

        # QLineEdit 선언 및 기본적인 설정
        self.LineEdit_id = QLineEdit(self)
        self.LineEdit_pw = QLineEdit(self)

        self.LineEdit_id.resize(330, 50)
        self.LineEdit_id.move(35, 120)
        self.LineEdit_id.setPlaceholderText("ID")

        self.LineEdit_pw.resize(330, 50)
        self.LineEdit_pw.move(35, 190)
        self.LineEdit_pw.setPlaceholderText('Password')
        self.LineEdit_pw.setEchoMode(QLineEdit.Password)

        # QLineEdit design 설정
        self.LineEdit_id.setStyleSheet("padding-left: 10px;"
                                       "border-radius: 15px;"
                                       "font: 20px Bahnschrift;"
                                       "font-weight: bold;")

        self.LineEdit_pw.setStyleSheet("padding-left: 10px;"
                                       "border-radius: 15px;"
                                       "font: 20px Bahnschrift;"
                                       "font-weight: bold;")

        # QPushButton 선언 및 기본 설정
        self.Button_login = QPushButton('login', self)
        self.Button_login.resize(200, 50)
        self.Button_login.move(95, 290)
        self.Button_login.clicked.connect(self.func_login)

        self.Button_new = QPushButton('회원가입', self)
        self.Button_new.move(154, 360)
        self.Button_new.clicked.connect(self.Click_new)

        # QPushButton design 설정
        self.Button_login.setStyleSheet("QPushButton:hover{border-radius: 15px; background-color: #4593D3;"
                                        "color: white; font: 30px Bahnschrift; font-weight: bold;}"
                                        "QPushButton{border-radius: 15px; background-color: #187aca;"
                                        "font: 30px Bahnschrift; color: white; font-weight: bold;}")
        self.Button_new.setStyleSheet(
            "color: black; background-color: #f8f8f8; border: 0px;"
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
        self.setFixedSize(400, 500)
        # QLabel 선언 및 기본적인 설정
        label_main = QLabel('Sign up', self)
        label_main.setAlignment(Qt.AlignCenter)
        label_main.resize(400, 80)

        # QLabel design 설정
        label_main.setStyleSheet("font: 50px MS PGothic; color: white; background-color: #187aca")
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
        LineEdit_name.setStyleSheet("padding-left: 10px;"
                                    "border-radius: 15px;"
                                    "font: 20px Bahnschrift;"
                                    "font-weight: bold;"
                                    )

        LineEdit_id.setStyleSheet("padding-left: 10px;"
                                  "border-radius: 15px;"
                                  "font: 20px Bahnschrift;"
                                  "font-weight: bold;")

        LineEdit_pw.setStyleSheet("padding-left: 10px;"
                                  "border-radius: 15px;"
                                  "font: 20px Bahnschrift;"
                                  "font-weight: bold;")

        LineEdit_pw_chek.setStyleSheet("padding-left: 10px;"
                                       "border-radius: 15px;"
                                       "font: 20px Bahnschrift;"
                                       "font-weight: bold;")
        LineEdit_name.show()
        LineEdit_pw_chek.show()
        LineEdit_pw.show()
        LineEdit_id.show()

        # QPushButton 선언 및 기본 설정
        Button_new = QPushButton('Sign up', self)
        Button_new.resize(200, 50)
        Button_new.move(95, 410)
        Button_new.clicked.connect(self.func_signup)

        Button_check_name = QPushButton('Check', self)
        Button_check_name.resize(70, 50)
        Button_check_name.move(295, 120)

        Button_check_id = QPushButton('Check', self)
        Button_check_id.resize(70, 50)
        Button_check_id.move(295, 190)

        # QPushButton design 설정
        Button_new.setStyleSheet("QPushButton:hover{border-radius: 15px; background-color: #4593D3;"
                                        "color: white; font: 25px Bahnschrift; font-weight: bold;}"
                                        "QPushButton{border-radius: 15px; background-color: #187aca;"
                                        "font: 25px Bahnschrift; color: white; font-weight: bold;}")
        Button_check_name.setStyleSheet("QPushButton:hover{border-radius: 15px; background-color: #4593D3;"
                                        "color: white; font: 15px Bahnschrift; font-weight: bold;}"
                                        "QPushButton{border-radius: 15px; background-color: #187aca;"
                                        "font: 15px Bahnschrift; color: white; font-weight: bold;}")
        Button_check_id.setStyleSheet("QPushButton:hover{border-radius: 15px; background-color: #4593D3;"
                                        "color: white; font: 15px Bahnschrift; font-weight: bold;}"
                                        "QPushButton{border-radius: 15px; background-color: #187aca;"
                                        "font: 15px Bahnschrift; color: white; font-weight: bold;}")

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