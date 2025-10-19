##2
class Cake :

    def __init__(self , flavor : str ,size : int , price : int ):
        self.flavor = flavor
        self.size = size
        self.price = price
    def describe (self):
        print(f"details : the cake is {self.flavor} & {self.size} & {self.price}")
cup_cake = Cake(flavor = "sweet", size = 5, price = 10)
cup_cake.describe()
