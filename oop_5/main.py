class Person:
   """Class for creation person"""

   def __init__(self, name, age):
       self.name = name
       self.age = age

   def print_attrs(self):
       print(f"<<<<<{str(self)}>>>>>")
       print(self.name, self.age)


person1 = Person('Tom', 18)
person1.print_attrs()

# print(Person.name, Person.age)
# Person.age = 50
# print(Person.name, Person.age)
# print(Person.__dict__)
# person1 = Person()
# person1._is_animal = False
# delattr(Person, 'age')
# print(Person.__dict__)
# print(hasattr(Person, 'age'))

# del Person.high
# print(Person.__dict__)
# print(hasattr(Person, 'high'))
# print(hasattr(person1, "name"))
# print(person1.__dict__)
# print(getattr(person1, "name"))
#
# person1.age = 59
# person1.color = 'black'
# print(person1.__dict__)
#
# setattr(person1, 'high', 100)
# print(person1.high)


person2 = Person("Oleg", 50)
print(person2)
person2.print_attrs()

class Points:
    """Class for create and set cords"""

    def __init__(self, x, y, z):
        self.y = y
        self.x = x
        self.z = z
        self.get_attrs()
        self.check_cords()

    def check_cords(self):
        for attr in self.__dict__:
            if getattr(self, attr, False) < 0 and not isinstance(self.__dict__[attr], str):
                print("Coord can't ne less than 0")
                setattr(self, attr, 0)
            elif getattr(self, attr, False) > 100 and not isinstance(self.__dict__[attr], str):
                print("Coord can't be great than 100")
                setattr(self, attr, 100)
        print(self.__dict__)

    def get_attrs(self):
        print(self.__dict__)

    def set_attr(self, x, y, z):
        self.x =x
        self.y = y
        self.z = z
        self.check_cords()

coord_1 = Points(-1, 101, 50)

print('________')
coord_1.set_attr(1000, 1000, 3)
