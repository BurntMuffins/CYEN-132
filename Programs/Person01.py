#####################################################################
# author: Aidan Schaubhut
# date: 3/11/23
# description: 
#####################################################################

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
class Person:
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

    @name.setter
    def name(self, value):
        if not (len(value) <= 2):
            self._name = 'player 1'
        else:
            self._name = value
    # X
    @property
    def x(self):
        return self._x

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

    @size.setter
    def size(self, value):
        if (value < 1):
            self._size = self._size
        else:
            self._size = value

    #################
    ### FUNCTIONS ###
    #################

    def goLeft(val):
        pass

    def goRight(val):
        pass

    def goUp(val):
        pass

    def goDown(val):
        pass

    def getDistance(other):
        pass

    def __str__(self):
        pass