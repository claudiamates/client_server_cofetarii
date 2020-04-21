class Serviciu():
    #serviceType = ""
    def __init__(self,t):
        self.serviceType = t

class Vanzare(Serviciu):
    def __init__(self,serviceType,items,price):
        super.__init__(serviceType)
        self.items = items
        self.totalPrice = price

    def calculatePrice(self,items):
        for i in items:
            self.totalPrice = self.totalPrice + i.price
    
    def returnRest(self,givenMoney):
        self.rest = givenMoney - self.totalPrice

class Reducere(Serviciu):
     def __init__(self,serviceType,procent):
        super.__init__(serviceType)
        self.procent = procent

     def applyR(self,currentPrice):
        self.newPrice = currentPrice - (self.procent/100)*currentPrice 