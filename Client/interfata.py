import sys
from PyQt5 import QtWidgets #import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5 import QtGui #import QIcon
from PyQt5 import QtCore #import pyqtSlot
from cofetariiGUI import AppC
from AdminGUI import AppD
import socket
from client import comunicate, validation

class AppL(QtWidgets.QMainWindow):

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
        # Create textbox
        self.textboxA = QtWidgets.QLineEdit(self)
        self.textboxA.move(100, 20)
        self.textboxA.resize(280,40)

        self.textboxB = QtWidgets.QLineEdit(self)
        self.textboxB.move(100, 80)
        self.textboxB.resize(280,40)

        
        # Create a button in the window
        self.buttonA = QtWidgets.QPushButton('LogIn as Employee', self)
        self.buttonA.move(20,140)
        self.buttonA.resize(200,40)

        self.buttonB = QtWidgets.QPushButton('LogIn as Administrator', self)
        self.buttonB.move(300,140)
        self.buttonB.resize(200,40)
        
        # connect button to function on_click
        self.buttonA.clicked.connect(self.on_clickA)
        self.buttonB.clicked.connect(self.on_clickB)
        self.show()
    
    #@pyqtSlot()
    def on_clickA(self):
        # usernameValue = self.textboxA.text()
        # passwordValue = self.textboxB.text()
        de = {'username':self.textboxA.text(), 'password': self.textboxB.text(),'usertype': 'angajat'}
        comunicate(de)
        # with open("Angajat.txt","r+") as f:
        #     if(("Username: "+usernameValue+"\n"+"Password: "+passwordValue) in f.read()):
        print("from interfata", validation)
        if(validation == 'valid'):
            QtWidgets.QMessageBox.question(self, 'Message - pythonspot.com', "succesfuly logged in" , QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
       #self.textbox.setText("")
            self.e = AppC()

    def on_clickB(self):
        # usernameValue = self.textboxA.text()
        # passwordValue = self.textboxB.text()
        de = {'username':self.textboxA.text(), 'password': self.textboxB.text(),'usertype': 'admin'}
        comunicate(de)
        #with open("Administrator.txt","r+") as f:
        if(validation == 'valid'):
            QtWidgets.QMessageBox.question(self, 'Message - pythonspot.com', "succesfuly logged in" , QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            self.e=AppD()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = AppL()
    sys.exit(app.exec_())
