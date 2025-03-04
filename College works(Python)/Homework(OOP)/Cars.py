class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand  # Марка транспортного средства
        self.model = model  # Модель
        self.year = year    # Год выпуска

    def Start_engine(self):
        print(f"{self.brand} {self.model} ({self.year}): Двигатель запущен.")

    def Stop_engine(self):
        print(f"{self.brand} {self.model} ({self.year}): Двигатель остановлен.")

    def Drive(self):
        print(f"{self.brand} {self.model} ({self.year}): Транспортное средство движется.")


class Car(Transport):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors 

    def Open_trunk(self):
        print(f"{self.brand} {self.model} ({self.year}): Багажник открыт.")

    def Drive(self):
        print(f"{self.brand} {self.model} ({self.year}): Легковой автомобиль едет по дороге.")


class Truck(Transport):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity  

    def Load_cargo(self):
        print(f"{self.brand} {self.model} ({self.year}): Грузовик загружен на {self.load_capacity} кг.")

    def Drive(self):
        print(f"{self.brand} {self.model} ({self.year}): Грузовик едет по трассе.")


class Motorcycle(Transport):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar  

    def Wheelie(self):
        print(f"{self.brand} {self.model} ({self.year}): Едет на одном колесе!!!!")

    def Drive(self):
        print(f"{self.brand} {self.model} ({self.year}): Мотоцикл едет по дороге.")



if __name__ == "__main__":
    car = Car("Хонда", "октавия)", 2020, 4)
    truck = Truck("Volvo", "какой-то", 2018, 5000)
    motorcycle = Motorcycle("Harley-Davidson", "(имя модели мотоцикла)", 2021, False)

    
    car.Start_engine()
    car.Drive()
    car.Open_trunk()
    car.Stop_engine()
    print()

    truck.Start_engine()
    truck.Drive()
    truck.Load_cargo()
    truck.Stop_engine()
    print()

    motorcycle.Start_engine()
    motorcycle.Drive()
    motorcycle.Wheelie()
    motorcycle.Stop_engine()