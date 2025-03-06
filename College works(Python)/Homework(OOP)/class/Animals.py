class Animal:
    def __init__(self, name):
        self.name = name

    def Eat(self):
        print(f"{self.name} кушает")

    def Walk(self):
        print(f"{self.name} ходит")

    def Drink(self):
        print(f"{self.name} пьет")

    def Make_sound(self):
        print(f"{self.name} издает какой-то звук")

    def Hunt(self):
        print(f"{self.name} охотится", end=" ")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def Break_vase(self):
        print(f"{self.name} разбила вазу!!!!!")

    def Crouch(self):
        print(f"{self.name} тихонько крадется")

    def Hunt(self):
        super().Hunt()
        print("на мышку")

    def Make_sound(self):
        print(f"{self.name} мяукает")


class Dog(Animal):
    def __init__(self, name, dog_size):
        super().__init__(name)
        self.dog_size = dog_size

    def Knock_owner(self):
        if self.dog_size > 2:
            print(f"{self.name} опрокинула хозяина!!!")
        else:
            print(f"{self.name} не опрокинула хозяина!! (она маленькая)")

    def Hunt(self):
        super().Hunt()
        print("на гуся")

    def Make_sound(self):
        print(f"{self.name} лает")


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def Fly(self):
        print(f"{self.name} летает!!!")

    def Hunt(self):
        super().Hunt()
        print("на жучка")

    def Make_sound(self):
        print(f"{self.name} чирикает")


if __name__ == "__main__":
    dog = Dog("Мухтар", 4)
    bird = Bird("Чижик")
    cat = Cat("Ya'qub Qamar Ad-Din Dibiazah")

    dog.Knock_owner()
    dog.Hunt()
    dog.Make_sound()
    print()

    bird.Fly()
    bird.Make_sound()
    bird.Hunt()
    print()

    cat.Break_vase()
    cat.Hunt()
    cat.Make_sound()