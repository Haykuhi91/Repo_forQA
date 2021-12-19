#TASK 1: PERSON/STUDENT
#1. Create a Python class Person with attributes: name and age of type string.
#2. Create a display() method that displays the name and age of an object created via the Person class.
#3. Create a child class Student which inherits from the Person class and which also has a section attribute.
#4. Create a method displayStudent() that displays the name, age, and section of an object created via the Student class.
#5. Create a student object via an instantiation on the Student class and then test the displayStudent method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, graduation_year):
        Person.__init__(self, name, age)
        self.graduation_year = graduation_year
    def displayStudent(self):

        print(self.name, self.age, self.graduation_year)

p1 = Student("Ara", 5, 2011)
p1.displayStudent()

"""TASK 2: Circle class
1. 

self.a = a
self.b = b
self.r = r

2. Define a Area() method of the class which calculates the area of the circle.
3. Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
4. Define a testBelongs() method of the class which allows to test whether a point A(x, y) belongs to the circle C(O, r) or not."""

class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r
    def Area(self):
        return 3.14 * self.r * self.r
    def Perimeter(self):
        return 2 * 3.14 * self.r
    def testBelongs(self):
        pass

CircleC = Circle()







