from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, ownerName, value):
        self.__ownerName = ownerName
        self.__value = value

    @abstractmethod
    def details(self):
        pass

    def get_ownerName(self):
        return self.__ownerName

    def get_value(self):
        return self.__value


class Pawn(ABC):
    def __init__(self, pawnID, pawnDate, redeemDate):
        self.__pawnID = pawnID
        self.__pawnDate = pawnDate
        self.__redeemDate = redeemDate

    def get_pawnID(self):
        return self.__pawnID

    def get_pawnDate(self):
        return self.__pawnDate

    def get_redeemDate(self):
        return self.__redeemDate


class Condition:
    def __init__(self, condition):
        self.__condition = condition

    def get_condition(self):
        return self.__condition

    def __str__(self):
        return self.__condition


class Jewelry(Item, Pawn):
    def __init__(self, ownerName, value, pawnID, pawnDate, redeemDate, condition):
        Item.__init__(self, ownerName, value)
        Pawn.__init__(self, pawnID, pawnDate, redeemDate)
        self.__condition = condition

    def details(self):
        return (f"Owner: {self.get_ownerName()}, Value: {self.get_value()}$, "
                f"Pawn ID: {self.get_pawnID()}, Pawn Date: {self.get_pawnDate()}, "
                f"Redeem Date: {self.get_redeemDate()}, Condition: {self.__condition}")

    def is_expensive(item):
        return item.get_value() > 3000


class Electronics(Item, Pawn):
    def __init__(self, ownerName, value, pawnID, pawnDate, redeemDate, condition):
        super().__init__(ownerName, value)
        Pawn.__init__(self, pawnID, pawnDate, redeemDate)
        self.__condition = condition

    def details(self):
        return (f"Owner: {self.get_ownerName()}, Value: {self.get_value()}$, "
                f"Pawn ID: {self.get_pawnID()}, Pawn Date: {self.get_pawnDate()}, "
                f"Redeem Date: {self.get_redeemDate()}, Condition: {self.__condition}")

    def is_expensive(item):
        return item.get_value() > 3000


condition1 = Condition("Good")
condition2 = Condition("Like New")

jewelry_item = Jewelry("Alex", 5000, "PWN123", "01.06", "30.06", condition1)
electronics_item = Electronics("Eli", 2000, "PWN456", "05.06", "05.07", condition2)

print(jewelry_item.details())
print(electronics_item.details())

print("Is the jewelry expensive?", Jewelry.is_expensive(jewelry_item))
print("Is the electronics expensive?", Electronics.is_expensive(electronics_item))
