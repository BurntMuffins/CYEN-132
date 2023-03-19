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
        self.color = self.setColor()
        self.surf = pygame.Surface(Item.size, Item.size)

    def setColor(self):
        self.color = choice(COLORS)

    def setSize(self):
        Item.size = randint(10, 100)
        self.surf = pygame.Surface(Item.size, Item.size)
    
    def update(self, pressedKey):
        match pressedKey:
            case [K_UP]:
                Item.goUp()
            case [K_DOWN]:
                Item.goDown()
            case [K_LEFT]:
                Item.goLeft()
            case [K_RIGHT]:
                Item.goRight()
            case [K_SPACE]:
                self.setColor()
                self.setSize()

    def setRandomPosition(self):
        Item.x = randint(0, WIDTH)
        Item.y = randint(0, HEIGHT)
    
    def getPosition(self) -> tuple:
        x = Item.x-Item.size/2
        y = Item.x-Item.size/2
        return x, y

    def __str__(self) -> str:
        return super().__str__() + f'color= {self.color}'




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

