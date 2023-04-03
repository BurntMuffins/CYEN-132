#####################################################################
# author: Aidan Schaubhut
# date: 4/3/23     
# description: A program that creates an Employee class with faculty and staff classes as subclasses
#####################################################################

# import the abc library to make abstract classes
from abc import ABC, abstractmethod

######################################################################
# An employee class. Its constructor takes the first name, last name and
# pay. It also has email and position as instance variables. It contains
# a single abstract method i.e. applyRaise, and a createEmail function
# that creates an appropriate email address from the employee's first
# and last names.
######################################################################

class Employee(ABC):
    def __init__(self, first, last, pay=20000) -> None:
        self.firstname = first
        self.lastname = last
        self.pay = pay
        self.position = None
        self.email = self.createEmail()

    ############################
    ## ACCESSORS AND MUTATORS ##
    ############################

    @property
    def firstname(self):
        return self._firstname
    
    # Sets the first name to have proper capitalization
    @firstname.setter
    def firstname(self, value):
        self._firstname = value.strip().capitalize()

    @property
    def lastname(self):
        return self._lastname
    
    # Sets the last name to have proper capitalization
    @lastname.setter
    def lastname(self, value):
        self._lastname = value.strip().capitalize()

    @property
    def pay(self):
        return self._pay
    
    # Checks that the given pay is at least $20,000
    @pay.setter
    def pay(self, value):
        if value < 20000:
            self._pay = 20000
        else:
            self._pay = value

    @property
    def email(self):
        return self._email
    
    # Checks for valid email input
    @email.setter
    def email(self, value):
        if "@latech.edu" in value:
            self._email = value
        else:
            self._email = self.email

    # Creates an email for the Employee using their first and last name
    def createEmail(self):
        return f"{self.firstname.lower()}.{self.lastname.lower()}@latech.edu"

    # A method that should be implemented by subclasses
    @abstractmethod
    def applyRaise(self, rate):
        raise NotImplementedError("subclasses should define 'applyRaise'")
        
    # Creates a string and returns it
    def __str__(self) -> str:
        return f'{self.lastname}, {self.firstname} ({self.email})'

######################################################################
# A faculty class is a subclass of the Employee class above. Its
# constructor receives both names as well as the position. The Faculty
# class also overrides the applyRaise function by multiplying the pay by
# the rate provided as an argument. It also slightly tweaks the __str__
# function in the super class.
######################################################################

class Faculty(Employee):
    def __init__(self, first, last, position) -> None:
        super().__init__(first, last, 50000)
        self.position = position

    # Applies a raise by multiplying the given rate by the pay
    def applyRaise(self, rate):
        if rate < 0:
            return
        else:
            self.pay *= rate

    # Uses the super class string and adds the position to the string
    def __str__(self) -> str:
        return super().__str__() + f" -- {self.position}"


######################################################################
# A Staff class is a subclass of the Employee class above. Its
# constructor only receives both names. It also overrides the applyraise
# function but adding the increase (provided as the argument) to the
# pay. It doesn't change anything else from the Employee class.
######################################################################

class Staff(Employee):
    def __init__(self, first, last) -> None:
        super().__init__(first, last, pay=40000)

    # Applies a raise by adding the provided rate to the pay
    def applyRaise(self, rate):
        if rate < 0:
            return
        else:
            self.pay += rate

