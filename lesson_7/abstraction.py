from abc import ABC, abstractclassmethod

class Car(ABC):
    """Car class"""

    def __init__(self, mark, cost):
        self.mark = mark
        self.cost = cost

    @abstractclassmethod
    def car_preview(self):
        pass

class Toyota(Car):

    def car_preview(self):
        print(f"Car {self.mark} costs {self.cost}")

class Mercedes(Car):

    def car_preview(self):
        print(f"Car {self.mark} costs {self.cost}")

class BMW(Car):
    pass

# toyota = Toyota("land", 1000)
# toyota.car_preview()
# mercedes = Mercedes("crossover", 5000)
# mercedes.car_preview()
# bmw = BMW("city_type", 4000)
# bmw.car_preview()

class Animal(ABC):

    @abstractclassmethod
    def move(self):
        pass

    @abstractclassmethod
    def eat(self):
        pass

class Cat(Animal):

    def __init__(self, color, age):
        self.color= color
        self.age = age

    def move(self):
        print(f"Cat with {self.color} color moves to ahead")

    def eat(self):
        print(f"Cat eats this food at {self.age} years ")

class Dog(Animal):

    def __init__(self, distance, food_type):
        self.distance = distance
        self.food_type = food_type

    def move(self):
        print(f"Dog walked {self.distance} km")

    def eat(self):
        print(f"Dof ate this {self.food_type} today")

class AnimalType(Animal):
    pass

class Bird(AnimalType):

    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"Bird {self.name} flies")

    def  eat(self):
        print(f"Bird {self.name} eats")

cat = Cat("red", 5)
cat.move()
cat.eat()

dog = Dog(100, "meat")
dog.move()
dog.eat()

bird = Bird("Dorry")
bird.move()
bird.eat()

an_1 = AnimalType()



