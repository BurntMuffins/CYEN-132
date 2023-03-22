class Animal:
    def __init__(self):
        """Constructs a new Animal"""

    def communicate(self):
        """How an animal communicates"""
        raise NotImplementedError("Abstract method communicate not implemented in subclass!")

# Shows the exmaple of having the communicate method, no error
class Birds(Animal):
    def __init__(self):
        """Constructs a new Bird"""

    def communicate(self):
        return "Tweet"

# Shows the example of not having communicate which results in an error.
class Dog(Animal):
    def __init__(self):
        """Constructs a new Dog"""

b1 = Birds()
print(b1.communicate())

d1 = Dog()
print(d1.communicate())