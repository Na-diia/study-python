
class Animal:
    """Class to create an animal"""
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        if self.species == 'Cat':
                print('Meow')
        elif self.species == 'Dog':
                print('Bark')
        elif self.species == 'Bird':
                print("Beautiful song")
        elif self.species == 'Fish':
                print('Bull')
        else:
                print("we don't know this animal")

animal1 = Animal('Balto', 'Dog', 5)
animal2 = Animal('Kotyhoroshko', 'Cat', 4)
animal1.make_sound()
animal2.make_sound()

# **Завдання 2: Робота з об'єктами**

class Restangle:
    """Class to present restangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.height * self.width
        print(area)

item1 = Restangle(10, 30)
item2= Restangle(5, 10)
item1.calculate_area()
item2.calculate_area()

