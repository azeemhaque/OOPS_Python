class Phone:
    def __init__(self,price,brand,camera):
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")
        super().buy()
s = SmartPhone(20000,"Oneplus",13)

s.buy()