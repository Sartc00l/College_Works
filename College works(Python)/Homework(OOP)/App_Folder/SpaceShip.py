class AbstractShip:
    def __init__(self,size,velocity,name):
        self.size = size
        self.velocity = velocity
        self.name = name
    def Fly(self):
        self.flyString = f"Корабль под именем - {self.name}\t"
    def Sit(self):
        self.sitString = f"Корабль {self.name} сел" 

class SmallShip(AbstractShip):
    def __init__(self,size,velocity,name,teamSize):
        velocity = "быстрая"
        super().__init__(size,velocity,name)
        self.teamSize = teamSize
    
    def Fly(self):
        self.flyString = f"Корабль {self.name} с командой размера {self.teamSize} едет на разведку"

class MediumShip(AbstractShip):
    def __init__(self, size, velocity, name,productCost):
        velocity = "средняя"
        super().__init__(size, velocity, name)
        self.productCost = productCost

    def Fly(self):
        self.flyString = f"Корабль {self.name} летит торговать,кол-во товара{self.productCost} со скоростью "

class BigShip(AbstractShip):
    def __init__(self, size, velocity, name, colonistsCount):
        velocity = "медленый"
        super().__init__(size, velocity, name)
        self.colonistsCount = colonistsCount



