class Card:
    """Class Card for user's card"""

    def __init__(self, card_number, balance):
        if self.__check_attribute_type(card_number, str):
            self.card_number = card_number
        if self.__check_attribute_type(balance, float):
            self.__balance = balance

    def get_card_data(self):
        return self.__dict__

    def set_card_data(self, attr, value):
        if self.__check_attribute_type(attr, should_be=str):
            self.__dict__[attr] = value
            return {attr: self.__dict__[attr]}
        else:
            print("Attribute must be string type!")

    def __check_attribute_type(self, attr, should_be):
        if type(attr) == should_be:
            return True
        else:
            raise TypeError(f"Attribute must be {should_be}")

user_card_1 = Card("4145 3436 7876 9163", 1000.0)
print(user_card_1.get_card_data())
print(user_card_1.set_card_data("card_number", "4145 0000 7876 9163"))
print(user_card_1.set_card_data("balance", 100))


