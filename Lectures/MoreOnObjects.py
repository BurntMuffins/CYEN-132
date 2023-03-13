
class Vehicle:
    def __init__(self, owner) -> None:
        self.tires = None
        self.engine = None
        self.owner = owner
        self.hasInsurence = True

    def __str__(self) -> str:
        return f"owner={self.owner}, tires={self.tires}, engine={self.engine}, insurence={self.hasInsurence}"


class Car(Vehicle):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.tires = 4
        self.engine = True

    def __str__(self) -> str:
        return f"Car; {super().__str__()}"
    
class Cycle(Vehicle):
    def __init__(self, owner, riders) -> None:
        super().__init__(owner)
        self.tires = 2
        self.riders = riders

    def __str__(self) -> str:
        return super().__str__() + f', riders = {self.riders}'

class Bicycle(Cycle):
    def __init__(self, owner, riders) -> None:
        super().__init__(owner, riders)
        self.tires = 2
        self.engine = False
        self.hasInsurence = False
    
    def __str__(self) -> str:
        return f"Bicycle; {super().__str__()}"
    
class Motorcycle(Cycle):
    def __init__(self, owner, riders) -> None:
        super().__init__(owner, riders)


    def __str__(self) -> str:
        return f"Motorcycle; {super().__str__()}"

    

c1 = Car('Aidan')
print(c1)

b1 = Bicycle('Tim', 1)
print(b1)

m1 = Motorcycle('John', 2)
print(m1)