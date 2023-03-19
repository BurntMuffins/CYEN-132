#####################################################################
# author: Aidan Schaubhut
# date: 3/11/23
# description: A program that will create a Person class with functions that can control the Person's position
#####################################################################

import math

# global Constants to restrict the maximum x and y values that a person object
# can have.
MAX_X = 800
MAX_Y = 600

# A class representing a person. A person can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left, 
# go right, go up and go down. A person also has a string function 
# that prints out their name location, and size. A person also has a 
# function that calculates the euclidean distance from another person 
# object.
class Item:
    def __init__(self, name:str='player 1', x:int=0, y:int=0):
        self.name = name
        self.x = x
        self.y = y
        self.size:float = 1

    ##############################
    ### ACCESSORS AND MUTATORS ###
    ##############################

    # NAME
    @property
    def name(self):
        return self._name

    # If the provided name is less than 2 it will be set as "player 1"
    @name.setter
    def name(self, value):
        if (len(value) <= 2):
            self._name = 'player 1'
        else:
            self._name = value
    # X
    @property
    def x(self):
        return self._x

    # If the provided x value is less than 0 it will be set to 0.
    # If the provided x value is greater than MAX_X it will be set to MAX_X
    @x.setter
    def x(self, value):
        if (value < 0):
            self._x = 0
        elif(value > MAX_X):
            self._x = MAX_X
        else:
            self._x = value
    
    # Y
    @property
    def y(self):
        return self._y
    
    # If the provided y value is less than 0 it will be set to 0.
    # If the provided y value is greater than MAX_Y it will be set to MAX_Y
    @y.setter
    def y (self, value):
        if (value < 0):
            self._y = 0
        elif(value > MAX_Y):
            self._y = MAX_Y
        else:
            self._y = value
    
    # SIZE
    @property
    def size(self):
        return self._size

    # If the provided size is less than 1, it will be set to the current size
    @size.setter
    def size(self, value):
        if (value < 1):
            self._size = self._size
        else:
            self._size = value

    #################
    ### FUNCTIONS ###
    #################

    # Decreases the person's x value by the given amount or by 1 if given None
    def goLeft(self, val=None):
        if val == None:
            self.x -= 1
        else:
            self.x -= val

    # Increases the person's x value by the given amount or by 1 if given None
    def goRight(self, val=None):
        if val == None:
            self.x += 1
        else:
            self.x += val

    # Decreases the person's y value by the given amount or by 1 if given None
    def goUp(self, val=None):
        if val == None:
            self.y -= 1
        else:
            self.y -= val

    # Increases the person's y value by the given amount or by 1 if given None
    def goDown(self, val=None):
        if val == None:
            self.y += 1
        else:
            self.y += val

    # Calculates the distance between to Person objects 
    def getDistance(self, other):
        return math.dist([self.x, self.y], [other.x, other.y])

    # Creates the string that is returned when a Person object is printed
    def __str__(self):
        return f'Person({self.name}):\tsize = {self.size},\tx = {self.x}\ty = {self.y}'