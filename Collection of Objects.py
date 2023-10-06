class Customer:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print("I am ",self.name," and I am ",self.age)

c1 = Customer("Ankit",31)
c2 = Customer("Malvika",34)
c3 = Customer("Rahul",32)

L = [c1,c2,c3]
for i in L:
    i.intro()

