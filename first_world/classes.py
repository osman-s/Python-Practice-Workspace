# Class: blueprint for creating new objects
# Object: instance of a class

# Class: Human
# Objects: John, Mary, Jack,

# 2 - Creating Classes
# 3 - Constructors
# 4. Class attributes vs. instance attributes
# 5. Class attributes vs. instance methods
# 6. Magic Methods

from abc import ABC, abstractmethod


class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
# print(type(point))
# print(isinstance(point, Point))
point.z = 10
point.draw()
print(point.default_color)
Point.zero().draw()
print(point)
# 7. Comparing methods
other = Point(1, 2)
print(point == other)

# 8. Performing Arithmetic Operations
print(point + other)
# 9. Making Custom Containers


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud["python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
# print(cloud.__tags)
# len(cloud)
# cloud["python"] = 10
# for tag in cloud:
#     print(tag)
# 10. Private Members
# print(cloud.__tags["PYTHON"])
print(cloud.__dict__)

# 11. Properties


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(10)
# product.price = -1
print(product.price)
# 13. Inheritance


class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def walk(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)

print(isinstance(m, object))
o = object()
print(issubclass(Mammal, Animal))
# 14. Method Overriding
print(m.age)
print(m.weight)
# 15. Multi-level Inheritance


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass
# Limit inherticance to 1 or 2 levels. To solve business solutions
# 16. Multiple Ineritance


class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):  # looks at first base class
    pass


manage = Manager()
manage.greet()
# 17. A good example of inheritance


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    pass #considered abract method 
# 18. Abstract Base Class - provide common code to dervs.
stream = MemoryStream()
stream.open()


