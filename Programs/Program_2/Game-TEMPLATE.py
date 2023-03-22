#####################################################################
# author: Aidan Schaubhut
# date: 3/19/23
# description: A game
#####################################################################
import pygame
from random import randint, choice
from Item import *
from Constants import *


class Person(pygame.sprite.Sprite, Item):
    def __init__(self) -> None:
        super().__init__()
        Item.__init__(self)
        self.setSize()
        self.setColor()
        self.setRandomPosition()

    # Function tht sets the color of the square
    def setColor(self):
        self.color = choice(COLORS)
        self.surf.fill((self.color))

    # Sets the size of the square
    def setSize(self):
        self.size = randint(10, 100)
        self.surf = pygame.Surface((self.size, self.size))
    
    # Updates the squares position
    def update(self, pressedKey):
        if pressedKey[K_UP]:
            # self.goUp()
            self.x -= 1
            print(self.x, self.y)
        elif pressedKey[K_DOWN]:
            self.goDown()
        elif pressedKey[K_LEFT]:
            self.goLeft()
        elif pressedKey[K_RIGHT]:
            self.goRight()
        elif pressedKey[K_SPACE]:
            self.setSize()
            self.setColor()

    def setRandomPosition(self):
        self.x = randint(0, WIDTH)
        self.y = randint(0, HEIGHT)
    
    def getPosition(self) -> tuple:
        x = self.x-self.size/2
        y = self.x-self.size/2
        return (x, y)

    def __str__(self) -> str:
        return super().__str__() + f' color= {self.color}'




########################### main game################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#####################################################################

# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a person object
p = Person()
RUNNING = True  # A variable to determine whether to get out of the
                # infinite game loop

while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            print(p)

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    p.update(pressedKeys)

    # fill the screen with a color
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()

