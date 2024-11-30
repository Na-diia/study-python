class A:
    """Class A"""
    name_a = "Class A is a parent class"
    is_main_class = True

    def print_hello(self):
        print("Hello from A!")

class B(A):
    """Class B"""
    name_b = "Class B is a child class"
    is_main_class = False

    def print_hello(self):
        print("Hello from B")


class C(B):
    """Class C"""
    pass

test_ex = C()
# test_ex.print_hello()

class Vehicle:
    """It's a base class for Vehicles"""

    def __init__(self, type, color, left_of_life=100):
        self.type = type
        self.color = color
        self.left_of_life = left_of_life

    def move(self):
        print("Your vehicle is moving")

    def fix(self):
        if self.left_of_life <= 50:
          print(f"{self.type} need to fix")
        else:
            print(f"Your {self.type} is good")


class Car(Vehicle):
    """Class Car"""
    def __init__(self, type, color,  left_of_life, cost=0):
        super().__init__(type, color,  left_of_life)
        self.cost = cost

    def move(self):
      print(f"{self.color} {self.type} is driving")
      print(f"Cost of the car is {self.cost}")

class Bicycle(Vehicle):
    """Class Bicycle"""

    def __init__(self, type, color, count_of_wheels, left_of_life):
        super().__init__(type, color,  left_of_life)
        self.count_of_wheels = count_of_wheels

    def move(self):
        print("You are so fast")

car_1 = Car(type="car", color="black", left_of_life=70, cost=10000)
car_1.move()
car_1.fix()

bicycle_1 = Bicycle(type="road_bicycle", color="red", left_of_life=30, count_of_wheels=2)
bicycle_1.move()
bicycle_1.fix()

class Counter:
    """Count of something"""

    def __init__(self, count_obj, type_obj, max_elements):
        self.count_obj = count_obj
        self.type_obj = type_obj
        self.max_elements = max_elements

    def counter(self):
        print(f"Type of object is {self.type_obj}")
        if  isinstance(self.count_obj, (list, dict, str, tuple)):
            count =  len(self.count_obj)
            if count > self.max_elements:
                print("Count elements of your object is more than need")
                print(f"More on {count - self.max_elements}")
            else:
                print(f"Count of elements : {count}")
        else:
            print("Your object must be iterable")

    def get_attrs(self):
        print(self.__dict__)

    def set_attr(self, attr, value):
       if hasattr(self, attr):
           setattr(self, attr, value)
       else:
           print("Check your attrs")

class ListElements(Counter):
    """Last of elements"""

    def __init__(self, count_obj, type_obj, max_elements):
        super().__init__( count_obj, type_obj, max_elements)
        pass

    def counter(self):
        super().counter()
        print("Operation was ended")
        
    def get_attrs(self):
        super().get_attrs()
        print("Operation was ended")


list_ex = ListElements([1, 2, 3, 4], list, 10)
# list_ex.counter()
# list_ex.get_attrs()
# list_ex.set_attr("count_obj", [1, 2, 3, 4, 5, 6])

class BaseInterface:
    """Base class"""

    def __init__(self):
       pass

    def get_attrs(self):
        pass

    def print_model(self):
        pass

    def count_of_price(self):
        pass

    def call_to_support(self):
        pass

class SiteInterface(BaseInterface):
    """Interface of our class"""
    
    def __init__(self, number, model, price):
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_model(self):
        print(f"Model of site is: {self.model}")

    def count_of_price(self):
        print(f"Count of site price : {self.price ** 2}")

    def call_to_support(self):
        print(f"Number of support is {self.number}")
        print(f"You can call from 8am to 19am")

site_user = SiteInterface(123456, 'shop', 1000)
site_user.print_model()
site_user.count_of_price()
site_user.call_to_support()
