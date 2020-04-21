import sys
from PyQt5 import QtWidgets #import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5 import QtGui #import QIcon
from PyQt5 import QtCore #import pyqtSlot
from client2 import comunica

class AppD(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        labelA = QtWidgets.QLabel(self)
        labelA.setText('DeleteAngjat:')
        labelA.move(20,20)

        labelB = QtWidgets.QLabel(self)
        labelB.setText('ViewEmployees:')
        labelB.move(20,80)

        self.textboxA = QtWidgets.QLineEdit(self)
        self.textboxA.move(200, 20)
        self.textboxA.resize(140,40)

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.move(20,240)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(1)

        self.buttonA = QtWidgets.QPushButton('Delete', self)
        self.buttonA.move(400,20)
        self.buttonA.resize(200,40)

        self.buttonB = QtWidgets.QPushButton('View', self)
        self.buttonB.move(400,80)
        self.buttonB.resize(200,40)

        self.buttonA.clicked.connect(self.on_clickA)

        self.buttonB.clicked.connect(self.on_clickB)

        self.show()

    def on_clickA(self):
        # with open("Angajat.txt","rw+") as f:
        #     if(("Username: "+self.textboxA.text()+"\n") in f.read()):
        #         f.seek(16,1)

        with open("Angajat.txt", "r+") as f:
            lines = f.readlines()
        with open("Angajat.txt", "w+") as f:
            for line in lines:
                if line.strip("\n") != "Username: "+self.textboxA.text():
                    f.write(line)

    def on_clickB(self):
        # with open("Angajat.txt","r+") as f:
        #       data=f.read()
        a = comunica(self.textboxA.text())
        myData = 'Username: '+a['username']+"Password: "+a['password']+"Firstname: "+a['fistdname']+'Lastname: '+a['lastname']+'Email: '+a['email']
        self.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem(myData))
        self.tableWidget.setColumnWidth(0,800)
        self.tableWidget.setRowHeight(0,1500)
        self.tableWidget.show()
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = AppD()
    sys.exit(app.exec_())
                
