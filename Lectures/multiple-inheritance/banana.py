class Fruit:
    def __init__(self) -> None:
        origin = ''
        isFresh = None

    def __str__(self) -> str:
        return f'origin: {self.origin}, isFresh = {self.isFresh}'

class SaleItem:
    def __init__(self) -> None:
        price = 0.0
        inventory = 0
        location = ''
    
    def sell(self, quantity):
        pass

    def buy(self, quantity):
        pass

    def move(self, location):
        pass

    def __str__(self) -> str:
        return f'price: {self.price}, inventory: {self.inventory}, location: {self.location}'

class Banana(SaleItem, Fruit):
    def __init__(self) -> None:
        super().__init__() # Fruit class is init'd first
        self.origin = 'USA'
        self.isFresh = True

        self.price = 5
        self.inventory = 5
        self.location = 'USA'

b1 = Banana()
print(b1)
