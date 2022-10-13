# Is a paradigm/style of programming where everythng is treated as an object
# Class - blueprint of an object
# object - instance of a class

class Iphone():
    brand = "apple"
    model = "Iphone X"
    color = "White"
    camera_MP = "26mp"
    hdd = "256 GB"
    platform = "IOS 14.1"


iphone1 = Iphone()
print(iphone1.brand)
print(iphone1.camera_MP)
iphone2 = Iphone()

schools = ["Changes", "Triple S", "Jamu", "Texas"]


# constructors, methods, inheritance
# constructor is a function inside a class, it is called the (__init__), that is used to initialize attributes inside a
# of a class.
# A class contains attributes/properties/states and behaviour/methods

class Book:
    def __init__(self, author, title, price, quantity):
        self.author = author
        self.title = title
        self.price = price
        self.quantity = quantity

    def show_book(self):
        print(
            f'The author is {self.author}, The title is {self.title}, Price of {self.title}, and quantity of {self.quantity}')


book1 = Book("$4500", "columbus", "House", "109")
book1.show_book()
print("         ")


# square

class Square:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        print(area)


square1 = Square(10, 10)
square1.area()

print("That's the area of a square")


# perimeter

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        perimeter = (self.width + self.height) * 2
        print(perimeter)


rectangle1 = Rectangle(10, 30)
rectangle1.perimeter()

print("That's the perimeter of a square")


# triangle

class Tetra:
    def __init__(self, base, height, hypotenuse):
        self.base = base
        self.height = height
        self.hypotenuse = hypotenuse

    def vol(self):
        vol = self.base * self.height * self.hypotenuse
        print(vol)


tetra1 = Tetra(5, 8, 10)
tetra1.vol()

print("That's the area of a tetra")


# circle

class Round:
    def __init__(self, pi, r):
        self.pi = pi
        self.r = r

    def area(self):
        area = self.pi * self.r ** 2
        print(area)


round1 = Round(3.142, 7)
round1.area()

print("That's the area of a circle")
