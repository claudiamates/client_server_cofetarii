class Ingredient():
    def __init__(self,name):
        self.name = name
        
class Reteta():
    listI = []
    def __init__(self,ingredientdsNumber,name):
        self.ingridientsNumber = ingredientdsNumber
        self.name = name
        self.listI = []
    
    def addIngridients(self,item):
        self.listI.append(item)

    def delIngridients(self,item):
        self.listI.remove(item)



class Prajitura():
    def __init__(self,name,price,numberA):
        self.name = name
        self.price = price
        self.numberAvailable = numberA

