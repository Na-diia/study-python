# Single Responsibility Principle - SRP
from abc import ABC, abstractclassmethod
from enum import Enum
class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def create_user(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def set_data_user(self, attr, value):
        if type(value)== str:
            self.__dict__[attr] = value
            return self.__dict__[attr]
        else:
            print("This type of value is wrong, we need str")

    def remove_user(self):
        del self.__dict__

user = User(name="Nadiia", email="nadiia@gmail.com", password="potter")
user.create_user(name="Nadiia", email="nadiia@gmail.com", password="potter")
print(user.__dict__)
user.set_data_user("name", "Michel")
print(user.__dict__)
user.remove_user()
print(user.__dict__)

# Open/Closed Principle - OCP

class Shape(ABC):

    @abstractclassmethod
    def calculate_area(self):
        pass

class Circle(Shape):

     def __init__(self, radius):
         self.radius = radius

     def calculate_area(self):
         print(f"{3.14 * self.radius * 2}")

class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        print(f"{self.a * self.b}")

class CalculateArea(Shape):

     def __init__(self, _radius, _a, _b, shape):
         self._radius = _radius
         self._a = _a
         self._b = _b
         self.shape = shape

     def calculate_area(self):

         if self.shape == 'Circle':
             print(f"Area of circle is {3.14 * self._radius * 2}")
         elif  self.shape == 'Rectangle':
             print(f"Area of rectangle is {self._a * self._b}")
         else:
             print("we don't know the area of this shape")
             
calculator_test = CalculateArea(0, 5, 9, "Rectangle")
calculator_test.calculate_area()
# Liskov Substitution Principle - LSP
class Figure(ABC):

    @abstractclassmethod
    def area(self):
        pass

class CircleFigure(Figure):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of circle is {3.14 * self.radius * self.radius}")

class RectangleFigure(Figure):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(f"Area of rectangle is {self.height * self.width}")

# Interface Segregation Principle - ISP
class NetworkPrinter(ABC):
    @abstractclassmethod
    def print_some(self):
      pass

class NetworkScan(ABC):
    @abstractclassmethod
    def scan(self):
       pass

class NetworkCopy(ABC):
    @abstractclassmethod
    def copy(self):
        pass

class Printer(NetworkPrinter):

    def print_some(self):
        print("Printer is working...")

class Scanner(NetworkScan):

    def scan(self):
        print("Scanner is working...")

printer = Printer()
printer.print_some()

scaner = Scanner()
scaner.scan()
# Dependency Inversion Principle - DIP
class Bands(Enum):
    QUEEN = 1
    LINKIN_PARK = 2
    PINK_FLOYD = 3

class BandMemberShipLookUp:
    @abstractclassmethod
    def find_all_musicians(self, bands):
        pass

class Musician:

    def __init__(self, name):
        self.name = name

class BandsMember(BandMemberShipLookUp):

    def __init__(self):
        self.band_membership = []

    def find_all_musicians(self, bands):
        for members in self.band_membership:
            if members[1] == bands:
                yield  members[0].name

    def add_band_membership(self, musician, band):
        self.band_membership.append((musician, band))

class Analysis:

    def __init__(self, band_member_ship_lookup):
        for musician in band_member_ship_lookup.find_all_musicians(Bands.QUEEN):
            print(f"{musician} is in the Queen")

musician_1 = Musician("Freddy")
musician_2 = Musician("Brian May")
musician_3 = Musician("John Deacon")

band_1 = BandsMember()
band_1.add_band_membership(musician_1, Bands.QUEEN)
band_1.add_band_membership(musician_2, Bands.QUEEN)
band_1.add_band_membership(musician_3, Bands.QUEEN)

Analysis(band_1)
