import sys
from PyQt5 import QtWidgets #import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5 import QtGui #import QIcon
from PyQt5 import QtCore #import pyqtSlot
from interfata import AppL
from users import Angajat, Admin
import socket
import pickle
from client import comunicate

HEDERSIZE =10

angajat = Angajat('a','a','a','a','a')
admin = Admin('a','a','a','a','a')

class App(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 600
        self.height = 600
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        labelA = QtWidgets.QLabel(self)
        labelA.setText('Username')
        labelA.move(20,20)

        labelB = QtWidgets.QLabel(self)
        labelB.setText('Password')
        labelB.move(20,80)

        labelC = QtWidgets.QLabel(self)
        labelC.setText('Name')
        labelC.move(20,140)

        labelD = QtWidgets.QLabel(self)
        labelD.setText('FirstName')
        labelD.move(20,200)

        labelE = QtWidgets.QLabel(self)
        labelE.setText('E-mail')
        labelE.move(20,260)
        # Create textbox
        self.textboxA = QtWidgets.QLineEdit(self)
        self.textboxA.move(100, 20)
        self.textboxA.resize(280,40)

        self.textboxB = QtWidgets.QLineEdit(self)
        self.textboxB.move(100, 80)
        self.textboxB.resize(280,40)

        self.textboxC = QtWidgets.QLineEdit(self)
        self.textboxC.move(100, 140)
        self.textboxC.resize(280,40)

        self.textboxD = QtWidgets.QLineEdit(self)
        self.textboxD.move(100, 200)
        self.textboxD.resize(280,40)

        self.textboxE = QtWidgets.QLineEdit(self)
        self.textboxE.move(100, 260)
        self.textboxE.resize(280,40)

          # Create a button in the window
        self.buttonA = QtWidgets.QPushButton('Register Employee', self)
        self.buttonA.move(20,320)
        self.buttonA.resize(200,40)

        self.buttonB = QtWidgets.QPushButton('Register Administrator', self)
        self.buttonB.move(300,320)
        self.buttonB.resize(200,40)
        
        # connect button to function on_click
        self.buttonA.clicked.connect(self.on_clickA)

        self.buttonB.clicked.connect(self.on_clickB)
        self.show()

    def on_clickA(self):
        # with open("Angajat.txt","a+") as f:
        #     f.write("Username: "+self.textboxA.text()+"\n")
        #     f.write("Password: "+self.textboxB.text()+"\n")
        #     f.write("Name: "+self.textboxC.text()+"\n")
        #     f.write("FirstName: "+self.textboxD.text()+"\n")
        #     f.write("E-mail: "+self.textboxD.text()+"\n")
        angajat = Angajat(self.textboxA.text(), self.textboxB.text(), self.textboxC.text(),self.textboxD.text(), self.textboxE.text())
        print(angajat.username)
        de = {'username' : angajat.username, 'password' : angajat.password, 'fistdname' : angajat.firstname, 'lastname' : angajat.lastname, 'email' : angajat.email, 'usertype' : 'angajat'}
        # msg = pickle.dumps(de)
        # msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8")+ msg
        # s.sendall(msg)
        
        #textboxValue = self.textboxA.text()
        QtWidgets.QMessageBox.question(self, 'Message - pythonspot.com', "Angajat inregistrat ", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        #self.textbox.setText("")
        #app2 = QtWidgets.QApplication(sys.argv)
        self.ex2 = AppL()
        comunicate(de)
        #sys.exit(2.exec_())
       # self.close()


    def on_clickB(self):
        # with open("Administrator.txt","a+") as g:
        #     g.write("Username: "+self.textboxA.text()+"\n")
        #     g.write("Password: "+self.textboxB.text()+"\n")
        #     g.write("Name: "+self.textboxC.text()+"\n")
        #     g.write("FirstName: "+self.textboxD.text()+"\n")
        #     g.write("E-mail: "+self.textboxD.text()+"\n")
        admin = Admin(self.textboxA.text(), self.textboxB.text(), self.textboxC.text(),self.textboxD.text(), self.textboxE.text())
        de = {'username' : admin.username, 'password' : admin.password, 'fistdname' : admin.firstname, 'lastname' : admin.lastname, 'email' : admin.email, 'usertype' : 'admin'}
        #textboxValue = self.textboxA.text()
        QtWidgets.QMessageBox.question(self, 'Message - pythonspot.com', "Administrator inregistrat: ", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        #self.textbox.setText("")
        self.e = AppL()
        comunicate(de)
        #e.show()
    
# def comunicate(d):
#     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     s.connect((socket.gethostname(),1235))
#     print(d)
#     msg = pickle.dumps(d)
#     msg = bytes(f'{len(msg):<{HEDERSIZE}}', "utf-8")+ msg
#     s.sendall(msg)
#     # full_msg =''
#     # new_msg = True
#     # msgR = s.recv(16)
#     # if new_msg:
#     #     msglen = int(msgR[:HEDERSIZE])
#     #     new_msg = False
#     # full_msg += msgR.decode("utf-8")
#     # if len(full_msg)-HEDERSIZE == msglen:
#     #     print(full_msg[HEDERSIZE:])
#     #     new_msg = True
#     #     full_msg = ''
#     s.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
