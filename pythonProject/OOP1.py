class Dog:
    def __init__(self, age, name):
        self.name = name
        self.age = age

dog1 = Dog(5,"Nick")
print(dog1.name)
print(dog1.age)

dog2 = Dog(7,"Rex")
print(dog2.age)

#class Door

class Door:
    def __init__(self, width, material):
        self.width = width
        self.material = material
door1 = Door(0.6, "wooden")
door2 = Door(0.5, "metal")
print(door2.width)

#class Taxi

class Taxi:
    def __init__(self, driver, color):
        self.driver = driver
        self.color = color

taxi1 = Taxi("Aram", "yellow")
taxi2 = Taxi("Hayk", "red")
print(taxi2.driver)

#class Hippy

class Hippo:
    count = 0
    def __init__(self, name, size):
        self.name = name
        self.size = size
        Hippo.count += 1

    def increase(self):
        self.size = self.size + 1
    def weight_down(self):
        self.size = self.size - 1



hippo1 = Hippo("Ara", 5)
hippo2 = Hippo("ata", 8)
print(Hippo.count)


