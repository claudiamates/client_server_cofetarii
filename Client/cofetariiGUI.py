import sys
import pandas as pd
from matplotlib import pyplot as plt
import numpy
import math
import xml.etree.cElementTree as ET
from PyQt5 import QtWidgets #import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5 import QtGui #import QIcon
from PyQt5 import QtCore #import pyqtSlot
import tkinter as tk
from tkinter import filedialog
#from controller.cofetariiControl import CofetariiC

csv_reader = pd.read_csv('Cofetari1.csv')
id_cofetarii = csv_reader['ID']
adrese = csv_reader['Adresa']
prajituri = csv_reader['Prajituri_disponibile']
nr_disponibile = csv_reader['Nr_prajituri_disponibile']
preturi =csv_reader['Pret']


class AppC(QtWidgets.QMainWindow):

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
        labelA.setText('Chose Adr:')
        labelA.move(20,20)

        labelB = QtWidgets.QLabel(self)
        labelB.setText('See Cake')
        labelB.move(20,80)

        labelC = QtWidgets.QLabel(self)
        labelC.setText('SeePrice')
        labelC.move(20,140)

        labelD = QtWidgets.QLabel(self)
        labelD.setText('Add Cake')
        labelD.move(20,200)

        labelE = QtWidgets.QLabel(self)
        labelE.setText('ChangePrice')
        labelE.move(20,260)

        labelF = QtWidgets.QLabel(self)
        labelF.setText('View Recipe:')
        labelF.move(20,320)

        # Create textbox
        self.comboboxA = QtWidgets.QComboBox(self)
        self.comboboxA.move(100, 20)
        self.comboboxA.resize(280,40)
        for adr in adrese:
            self.comboboxA.addItem(adr)
        self.comboboxA.currentIndexChanged.connect(self.selection)

        self.comboboxB = QtWidgets.QComboBox(self)
        self.comboboxB.move(100, 80)
        self.comboboxB.resize(280,40)
        # self.comboboxB.addItems(["Prajitura cu mere","TreiCiocolate","Tiramisu"])

        self.comboboxC = QtWidgets.QComboBox(self)
        self.comboboxC.move(100, 140)
        self.comboboxC.resize(280,40)

        self.textboxC = QtWidgets.QLineEdit(self)
        self.textboxC.move(100, 200)
        self.textboxC.resize(280,40)

        # self.textboxD = QtWidgets.QLineEdit(self)
        # self.textboxD.move(100, 200)
        # self.textboxD.resize(280,40)

        self.textboxE = QtWidgets.QLineEdit(self)
        self.textboxE.move(100, 260)
        self.textboxE.resize(280,40)


         # Create a button in the window
        self.buttonA = QtWidgets.QPushButton('Add', self)
        self.buttonA.move(400,200)
        self.buttonA.resize(200,40)

        # self.buttonB = QtWidgets.QPushButton('Remove', self)
        # self.buttonB.move(400,200)
        # self.buttonB.resize(200,40)

        self.buttonC = QtWidgets.QPushButton('Change', self)
        self.buttonC.move(400,260)
        self.buttonC.resize(200,40)

        self.buttonD = QtWidgets.QPushButton('ViewRecipe', self)
        self.buttonD.move(400,320)
        self.buttonD.resize(200,40)

        self.buttonE = QtWidgets.QPushButton('PriceBarChart', self)
        self.buttonE.move(20,380)
        self.buttonE.resize(200,40)

        self.buttonF = QtWidgets.QPushButton('DisponibilityBarChart', self)
        self.buttonF.move(20,440)
        self.buttonF.resize(200,40)

        self.buttonG = QtWidgets.QPushButton('DisponibilityPieChart', self)
        self.buttonG.move(300,440)
        self.buttonG.resize(200,40)

        self.buttonH = QtWidgets.QPushButton('PriceRingChart', self)
        self.buttonH.move(300,380)
        self.buttonH.resize(200,40)

        # connect button to function on_click
        self.buttonA.clicked.connect(self.on_clickA)

        # self.buttonB.clicked.connect(self.on_clickB)

        self.buttonC.clicked.connect(self.on_clickC)

        self.buttonD.clicked.connect(self.on_clickD)

        self.buttonE.clicked.connect(self.on_clickE)

        self.buttonF.clicked.connect(self.on_clickF)

        self.buttonG.clicked.connect(self.on_clickG)

        self.buttonH.clicked.connect(self.on_clickH)


        self.show()

    def selection(self):
        # if(self.comboboxA.currentText()=="B-ld 21 Decembrie 1989 nr.24, Cluj-Napoca"):
        #     self.comboboxB.clear()
        #     self.comboboxB.addItems(["Prajitura cu mere","TreiCiocolate","Tiramisu"])
        # if(self.comboboxA.currentText()=="str Eroilor nr21, Floresti"):
        #     self.comboboxB.clear()
        #     self.comboboxB.addItems(["Prajitura cu lamaie","Prajitura cu fructe de padure","Tiramisu"])
        # if(self.comboboxA.currentText()=="str Lalelelor nr.4, Bucuresti"):
        #     self.comboboxB.clear()
        #     self.comboboxB.addItems(["Prajitura cu ananas","Prajitura cu fructe de padure","TreiCiocolate"])
        # if(self.comboboxA.currentText()=="str Trandafirilor nr.5, Satu Mare"):
        #     self.comboboxB.clear()
        #     self.comboboxB.addItems(["Prajitura cu ananas","Prajitura cu fructe de padure","TreiCiocolate"])
        for i in id_cofetarii:
            if(self.comboboxA.currentText()==adrese[i]):
                self.comboboxB.clear()
                self.comboboxB.addItems(prajituri[i].split(';'))
                self.comboboxC.clear()
                self.comboboxC.addItems(preturi[i].split(';'))
        
       


    def on_clickA(self):
        praji = ''
        disp = ''
        pre = ''
        praji = praji+self.textboxC.text()+";"
        disp =disp + "50;"
        pre = pre + "4;"
        self.comboboxB.addItem(self.textboxC.text())
        #isponibile.append('50')
        for i in id_cofetarii:
            if(self.comboboxA.currentText() == adrese[i]):
                praji = praji+ prajituri[i]
                disp = disp + nr_disponibile[i]
                pre = pre + preturi[i]
                prajituri[i] = praji
                nr_disponibile[i] = disp
                preturi[i] = pre

        newCSV = ({'ID' : id_cofetarii,
                    'Adresa': adrese,
                    'Prajituri_disponibile' : prajituri,
                    'Nr_prajituri_disponibile' : nr_disponibile,
                    'Pret': preturi})
    
        print(praji)
        print(disp)
        df = pd.DataFrame(newCSV)
        df.to_csv('C:\\Users\\Asus\\Desktop\\Mates_Claudia\\Client\\Cofetari1.csv',index = False, header=True)
        df.to_json('C:\\Users\\Asus\\Desktop\\Mates_Claudia\\Client\\newCofetarii.json', orient='records', lines=True)

        for i in id_cofetarii:
            if(self.comboboxA.currentText() == adrese[i]):
                root = ET.Element(self.comboboxA.currentText())
                doc = ET.SubElement(root, "doc")

                ET.SubElement(doc, "field1", name='prajituri').text = praji[0] + praji [1] + praji[2] + praji[3]
                ET.SubElement(doc, "field2", name="disponibilitate").text = disp[0] + disp[1] + disp[2] + disp[3]

                tree = ET.ElementTree(root)
                tree.write("Cofetarii.xml")
    
        #textboxValue = self.textboxA.text()
        QtWidgets.QMessageBox.question(self, 'Message - pythonspot.com', "Added Item ", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        #self.textbox.setText("")

    # def on_clickB(self):
        
    #     #textboxValue = self.textboxA.text()
    #     QtWidgets.QMessageBox.question(self, 'Message - pythonspot.com', "Removed Item: ", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
    #     #self.textbox.setText("")
    #     self.close()
    #     # app2 = QtWidgets.QApplication(sys.argv)
    #     # ex2 = AppL()
    #     # sys.exit(app2.exec_())
    
    def on_clickC(self):
        procent = self.textboxC.text()
        f = []
        for i in id_cofetarii:
            d = nr_disponibile[i].split(';')
            for x in d:
                f.extend(x-(x*10)/100)

        self.comboboxC.clear()
        for j in f:
            self.comboboxC.addItems(j)
        QtWidgets.QMessageBox.question(self, 'Message - pythonspot.com', "Changed: ", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def on_clickD(self):
        # root = tk.Tk()
        # root.withdraw()
        # file_path = filedialog.askopenfilename()
        ckakeName = self.comboboxB.currentText() + ".txt"
        with open(ckakeName,"r+") as f:
            data=f.read()
            self.tableWidget = QtWidgets.QTableWidget()
            self.tableWidget.move(20,240)
            self.tableWidget.setRowCount(1)
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem(data))
            self.tableWidget.setColumnWidth(0,800)
            self.tableWidget.setRowHeight(0,1500)
            self.tableWidget.show()
        QtWidgets.QMessageBox.question(self, 'Message - pythonspot.com', "Recipe found", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def on_clickE(self):
        pret =[]
        praji = []
        plt.style.use("fivethirtyeight")

        for i in id_cofetarii:
            pret.extend(preturi[i].split(';'))
            praji.extend(prajituri[i].split(';'))
        
        print(praji)
        print(pret)
        plt.barh(praji,pret)
        plt.ylabel("Prajituri")
        plt.xlabel("Preturi")
        plt.title("Statistici preturi")
        plt.show()

    def on_clickF(self):
        praji = []
        disp =[]
        plt.style.use("fivethirtyeight")

        for i in id_cofetarii:
            praji.extend(prajituri[i].split(';'))
            disp.extend(nr_disponibile[i].split(';'))
        disp.sort()
        # print(praji)
        plt.barh(praji,disp)
        plt.ylabel("Prajituri")
        plt.xlabel("Disponibilitate")
        plt.title("Statistici disponibilitate")
        plt.show()

    def on_clickG(self):
        disp =[]
        praji = []
        plt.style.use("fivethirtyeight")

        for i in id_cofetarii:
            if(self.comboboxA.currentText() == adrese[i]):
                disp.extend(nr_disponibile[i].split(';'))
                praji.extend(prajituri[i].split(';'))
        
        # print(praji)
        plt.pie(disp,labels=praji, wedgeprops={'edgecolor': 'black'},autopct='%1.1f%%')
        plt.tight_layout()
        plt.title("Disponibilitate in cofetaria aflata la adresa: "+self.comboboxA.currentText())
        plt.show()

    def on_clickH(self):
        pret =[]
        praji = []
        plt.style.use("fivethirtyeight")

        for i in id_cofetarii:
            pret.extend(preturi[i].split(';'))
            praji.extend(prajituri[i].split(';'))
        
        # print(praji)
        plt.polar()
        plt.barh(praji,pret,0.25,math.radians(150))
        plt.title("Statistici preturi")
        plt.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = AppC()
    sys.exit(app.exec_())
