from enum import Enum
from abc import ABC, abstractclassmethod

class Product(Enum):
    SHIRT = 1
    TSHIRT = 2
    PANTS = 3

class DiscountCalculator:

    def __init__(self, product_type, cost):
        self.product_type = product_type
        self.cost = cost

    def get_discount(self):
        if self.product_type == Product.SHIRT:
            return self.cost - (self.cost * 0.10)
        elif self.product_type == Product.TSHIRT:
            return self.cost - (self.cost * 0.15)
        elif self.product_type == Product.PANTS:
            return self.cost - (self.cost * 0.20)

ds_shirt = DiscountCalculator(Product.SHIRT, 100)
print(ds_shirt.get_discount())
ds_tshirt = DiscountCalculator(Product.TSHIRT, 100)
print(ds_tshirt.get_discount())
ds_pants = DiscountCalculator(Product.PANTS, 100)
print(ds_pants.get_discount())

class DiscountCalculate(ABC):

    @abstractclassmethod
    def get_discounted_product(self):
        pass

class DiscountCalculatorShirt(DiscountCalculate):

    def __init__(self, cost):
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.10)


class DiscountCalculatorTShirt(DiscountCalculate):

    def __init__(self, cost):
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.15)


class DiscountCalculatorPants(DiscountCalculate):

    def __init__(self, cost):
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.20)

dc_shirt = DiscountCalculatorShirt(100)
print(dc_shirt.get_discounted_product())
dc_tshirt = DiscountCalculatorTShirt(100)
print(dc_tshirt.get_discounted_product())
dc_pant = DiscountCalculatorPants(100)
print(dc_pant.get_discounted_product())










