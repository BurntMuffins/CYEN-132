#####################################################################
# author: Aidan Schaubhut
# date: 4/23/23
# description: A game where a wizard shoots a spider
#####################################################################

import pygame
from Constants import *
from random import randint

class Bullet(pygame.sprite.Sprite):
    # Creates the bullet based off the player's position
    def __init__(self, position):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((10, 20))
        self.surf.fill(pygame.Color('yellow'))
        self.rect = self.surf.get_rect()
        self.rect.center = position

    # Moves the bullet and is removed if it reaches the top of the screen
    def update(self):
        self.rect.move_ip(0, -10)
        if self.rect.bottom < 0:
            self.kill()

        # Check for collisions with enemy sprites
        collisons = pygame.sprite.spritecollide(self, enemies, False)
        for sprite in collisons:
            if sprite != self:
                # Kills the bullet and the enemy. Adds one to the players score
                # and then creates a new enemy for the player to fight
                self.kill()
                sprite.kill()
                player.score += 1
                Enemy.add_enemy()

class Player(pygame.sprite.Sprite):
    # Initializes the player. Loads the image. Declares variables to be used in later methods
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load('wizard.png').convert()
        self.surf = pygame.transform.scale(self.surf, (70, 70))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT))
        self.last_time_fired = 0
        self.score = 0
        self.lives = 3

    def update(self, pressed_keys):
        # Collison with enemy
        if pygame.sprite.spritecollideany(player, enemies):
            self.lives -= 1
            self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT))

        # Move based on user keystrokes
        player_speed = 5
        # This is used to determine the time since the last bullet was fired 
        current_time = pygame.time.get_ticks()

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -player_speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, player_speed)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-player_speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(player_speed, 0)
        if pressed_keys[K_SPACE] and current_time - self.last_time_fired > 500:
            bullet = Bullet(self.rect.center)
            all_sprites.add(bullet)
            bullets.add(bullet)
            self.last_time_fired = current_time

        # Keep the player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        

class Enemy(pygame.sprite.Sprite):
    # Creates an enemy with a set speed
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("spider.png").convert()
        self.surf = pygame.transform.scale(self.surf, (90, 90))
        self.rect = self.surf.get_rect(center=(-36, randint(30, 150)))
        self.speed = 4

    # Moves the spider across the screen
    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right > WIDTH:
            self.kill()
            self.add_enemy()
            player.lives -= 1

    # a method to add the new enemy
    @classmethod
    def add_enemy(cls):
        new_enemy = cls()
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)

# Init pygame and the screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create the player
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Font for the 
font = pygame.font.Font(None, 30)

# A clock to determine frame rate
clock = pygame.time.Clock()

running = True

Enemy.add_enemy()
# Main loop
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        if event.type == QUIT:
            running = False
        
        if player.lives <= 0:
            running = False
            
    # Variable for tracking the keys pressed
    pressed_keys = pygame.key.get_pressed()

    # Update all of the sprites
    player.update(pressed_keys)
    bullets.update()
    enemies.update()
    
    # Fill the screen
    screen.fill((0,0,0))

    # Display all the score board and lives
    text = font.render(f"Lives: {player.lives}   Score: {player.score}", True, (255,255,255))
    screen.blit(text, (5, HEIGHT-30))

    # Display all of the sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

    clock.tick(30)

