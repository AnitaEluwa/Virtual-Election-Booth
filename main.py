

from PyQt5 import QtWidgets, QtGui

import requests
from views import view



class vote(QtWidgets.QMainWindow,view.Ui_MainWindow):
    def __init__(self):
        super(vote,self).__init__()
        self.setupUi(self)
        # sign button in our appliction when you clicked it call the log_in fuction
        self.sign_ptn.clicked.connect(self.login_fun)
        # send button in our appliction when you clicked it call the sender_voter fuction
        self.send_vote_2.clicked.connect(self.sender_voter)
        self.select_vote=""
        self.show()

    # log in function is used to enable user to vaildate user log in 
    def login_fun(self):
        user_name = self.line_mail_2.text()
        user_pass = self.line_pass_2.text()
        global token
        data = {'user_name': user_name, "user_password": user_pass}
        response = requests.post("http://127.0.0.1:8000/get_token/", data=data)
        token = response.text  # this contain the token you ganna use it during the vote

        # check if the user already exist if exist so go to the next page of app
        if token != "user not existed":
            self.stackedWidget.setCurrentWidget(self.page_2)
            return token
        else:
            # else show a message box that contain warring message to the user
            msg=QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle(" Warnning ")
            # this is the message that will appear to user
            msg.setText("Please check your username or password .and try again")
            # execute this message (mean show the warrning message to the user)
            msg.exec_()

        # print(token)

    # this function is responsable for sending real vote to ctf_server
    def sender_voter(self):
        # self.person_1.isChecked() check if  you click on person1 radio button  
        if self.person_1.isChecked() :
            self.select_vote = "person1"
        # self.person_1.isChecked() check if  you click on person2 radio button  
        elif self.person_2.isChecked() :
            self.select_vote = "person2"
        # when u do not click on any radio button option you must get warnning message
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            # this is the title of message box
            msg.setWindowTitle(" Warnning ")
            # this is the message that will appear in message box
            msg.setText(" Please choise option ")
            msg.exec_()
        # data that will be sent to ctf_server ('user_token', 'vote_vote')
        data = {'token': token, "vote_name": self.select_vote}
        response = requests.post("http://127.0.0.1:7000/vote_for/", data=data)
        # print(response)
        # when u send vote exit the application
        application.exit()

application = QtWidgets.QApplication([])
vote_app = vote()
# execute our application
application.exec_()

# pyuic5 forms/form.ui -o views/view.py