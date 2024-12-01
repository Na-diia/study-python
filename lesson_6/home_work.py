

class Vehicle:
    """Base class for different vehicles"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This made by {self.make}, model is {self.model}, {self.year} year ")

class Car(Vehicle):

    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print("Your car's engine is starting")

    def display_info(self):
        print(f"This made by {self.make}, model is {self.model}, {self.year} year, type of fuel: {self.fuel_type}")

class Motorcycle(Vehicle):

    def __init__(self, make, model, year, number_of_petroleum):
        super().__init__(make, model, year)
        self.number_of_petroleum = number_of_petroleum

    def get_info(self):
        print(f"This motorcycle is {self.year}, model is {self.model}")

    def display_info(self):
        print(f"This made by {self.make}, model is {self.model}, {self.year} year, number of petroleum : {self.number_of_petroleum}")


class Bicycle(Vehicle):

    def __init__(self, make, model, year, fail):
        super().__init__(make, model, year)
        self.fail = fail

    def number_of_fail(self):
        print(f"I fail from this bicycle {self.fail} time")

    def display_info(self):
        print(f"This made by {self.make}, model is {self.model}, {self.year} year, fail: {self.fail}")


car_1 = Car("Ukraine", "Super-dragon", 2024, "super-cool")
bicycle_1 = Bicycle("France", "Mountain-travel", 2020, 6)
motorcycle_1 = Motorcycle("German", "Hero", 1998, 50)

print(car_1.__dict__)
print(bicycle_1.__dict__)
print(motorcycle_1.__dict__)

list_of_vehicles = [car_1, motorcycle_1, bicycle_1]

for vehicle in list_of_vehicles:
    vehicle.display_info()
    print("_____________")

