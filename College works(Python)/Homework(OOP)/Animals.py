class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} кушает")

    def walk(self):
        print(f"{self.name} ходит")

    def drink(self):
        print(f"{self.name} пьет")

    def make_sound(self):
        print(f"{self.name} издает какой-то звук")

    def hunt(self):
        print(f"{self.name} охотится", end=" ")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def break_vase(self):
        print(f"{self.name} разбила вазу!!!!!")

    def crouch(self):
        print(f"{self.name} тихонько крадется")

    def hunt(self):
        super().hunt()
        print("на мышку")

    def make_sound(self):
        print(f"{self.name} мяукает")


class Dog(Animal):
    def __init__(self, name, dog_size):
        super().__init__(name)
        self.dog_size = dog_size

    def knock_owner(self):
        if self.dog_size > 2:
            print(f"{self.name} опрокинула хозяина!!!")
        else:
            print(f"{self.name} не опрокинула хозяина!! (она маленькая)")

    def hunt(self):
        super().hunt()
        print("на гуся")

    def make_sound(self):
        print(f"{self.name} лает")


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f"{self.name} летает!!!")

    def hunt(self):
        super().hunt()
        print("на жучка")

    def make_sound(self):
        print(f"{self.name} чирикает")



if __name__ == "__main__":
    dog = Dog("Мухтар", 4)
    bird = Bird("Чижик")
    cat = Cat("Ya'qub Qamar Ad-Din Dibiazah")

    dog.knock_owner()
    dog.hunt()
    dog.make_sound()
    print()

    bird.fly()
    bird.make_sound()
    bird.hunt()
    print()

    cat.break_vase()
    cat.hunt()
    cat.make_sound()