class Cofetarie():
    menu = []
    schedule = " "
    adress =  " "
    id = 0
    def __init__(self,id,adress,meniu,schedule):
        self.id = id
        self.adress = adress
        self.menu = []
        self.schedule = schedule

    def addItemToMenu(self,prajitura):
        self.menu.append(prajitura)

    def deleteFromMenu(self,prajitura):
        self.menu.remove(prajitura)
   
    def changeSchedule(self,schedule):
        self.schedule = schedule

class ConstructorLantCofetarii():
    def __init__(self,listaCofatarii):
        self.listaCofatarii= []

class LantCofetarii(ConstructorLantCofetarii):
    def __init__(self,coetarii):
        self.cofetarii = []
    def addCofetarie(self,c):
        self.cofetarii.append(c)
    