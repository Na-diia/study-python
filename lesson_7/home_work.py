# Завдання 1: Інкапсуляція
class User:
    """Class for creating users"""

    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_data(self):
        return  self.__dict__

    def set_data(self, attr, value):
        if type(value) == str:
            self.__dict__[attr] = value
            return {attr: self.__dict__[attr]}
        else:
            print("This type isn't string")

user_1 = User("Dmytro", "dmytro@gmail.com", "potter")
user_1.__dict__
print(user_1.get_data())
user_1.set_data("_User__name", "Vira")
print(user_1.get_data())
# Завдання 2: Абстракція
from abc import ABC, abstractclassmethod

class Shape(ABC):

    @abstractclassmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print(f"Area of this circle is {3.14 * self.radius * 2}")

class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        print(f"The area of this rectangle is {self.a * self.b}")

circle = Circle(6)
circle.calculate_area()

rectangle = Rectangle(10, 5)
rectangle.calculate_area()

