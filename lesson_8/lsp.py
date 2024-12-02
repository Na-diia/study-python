class Car:

    def __init__(self, type):
        self.type = type
        self.properties = {}

    def set_properties(self, cost, color, capacity):
        self.properties = {"color": color, "cost": cost, "capacity": capacity}

    def get_properties(self):
         return self.properties


class PetrolCar(Car):

    def __init__(self, type):
        self.type = type
        self.properties = {}

car = Car("Toyota")
car.set_properties(10000, "red", 4)
print(car.get_properties())

petrol_car = PetrolCar("Volvo")
petrol_car.set_properties(5000, "red", 6)
print(petrol_car.get_properties())

cars = [car, petrol_car]

def get_concret_color_car(color):
    count = 0
    mark_cars = []
    for car in cars:
        if car.properties["color"] == "red":
            count +=1
            mark_cars.append(car.type)
    print(f"Count of {color} cars is {count}\nCar marks: {mark_cars}")

get_concret_color_car("red")