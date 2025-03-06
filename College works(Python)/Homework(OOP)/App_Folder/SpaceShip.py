class AbstractShip:
    def __init__(self,size,velocity,name):
        self.size = size
        self.velocity = velocity
        self.name = name
    def __str__(self):
        return f"{self.name}"
    def Fly(self):
        self.flyString = f"Корабль под именем - {self.name}\t"
        return self.flyString
    def Sit(self):
        self.sitString = f"Корабль {self.name} сел" 
        return self.sitString

class SmallShip(AbstractShip):
    def __init__(self,name,teamSize,size="маленькая",velocity="быстрая"):
   
        super().__init__(size,velocity,name)
        self.teamSize = teamSize
    def __str__(self):
        return f"{self.name}"
    def Fly(self):
        self.flyString = f"Корабль {self.name} с командой размера {self.teamSize} едет на разведку"
    

class MediumShip(AbstractShip):
    def __init__(self,name,productCost,size="средняя",velocity="средняя"):
        super().__init__(size,velocity,name)
        self.productCost = productCost
    def __str__(self):
        return f"{self.name}"
    def Fly(self):
        self.flyString = f"Корабль {self.name} летит торговать,кол-во товара{self.productCost} c скоростью "

class BigShip(AbstractShip):
    def __init__(self,name, colonistsCount,size="большая",velocity="медленная"):
        
        super().__init__(size, velocity, name)
        self.colonistsCount = colonistsCount
    def __str__(self):
        return f"{self.name}"



