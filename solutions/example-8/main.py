# Example 7

# Import and initialize pygame
import pygame
from random import randint, choice
from GameObject import GameObject
from Apple import Apple
from Strawberry import Strawberry
from Bomb import Bomb
from Player import Player
from Cloud import Cloud
from AnimatedObject import AnimatedObject
from Explosion import Explosion
from Pop import Pop
from Fruit import Fruit
from PointsSprite import PointsSprite
from ScoreBoard import ScoreBoard

pygame.init()
pygame.font.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])

# ---------------------------------------
# make instances 

# Make a group
all_sprites = pygame.sprite.Group()
# make a fruits Group
fruit_sprites = pygame.sprite.Group()
# Explosion Group
explosion_sprites = pygame.sprite.Group()

# Make Clouds
all_sprites.add(Cloud())
all_sprites.add(Cloud())
all_sprites.add(Cloud())

# Make Fruit instances
for n in range(1, 3):
  fruit = Fruit()
  fruit_sprites.add(fruit)
  all_sprites.add(fruit)

# fruit_sprites.add(fruit)

# make instance of Player
player = Player()

# make bomb
bomb = Bomb()

# Add sprites to group
all_sprites.add(player)
all_sprites.add(bomb)

# Score
score = ScoreBoard(30, 30, 0)
all_sprites.add(score)

# Get the clock
clock = pygame.time.Clock()

def make_explosion(x, y):
  explosion = Explosion(x, y)
  explosion_sprites.add(explosion)


def make_pop(x, y):
  explosion = Pop(x, y)
  explosion_sprites.add(explosion)


# Create the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()

  # Clear screen
  screen.fill((170, 230, 255))

  # Move and render Sprites
  for entity in all_sprites:
    entity.move()
    entity.render(screen)
    if entity != player: 
      pass

  # Check Colisions
  # Fruit Player Collisions
  fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
  if fruit:
    if fruit.flavor == "sweet":
      make_pop(fruit.x, fruit.y)
      # Make some text
      points = PointsSprite(fruit.x, fruit.y, 100)
      score.update(100)
      all_sprites.add(points)
      fruit.reset()
    else: 
      make_pop(player.x, player.y)
      player.stun()
      fruit.reset()

  # Fruit bomb collisions
  fruit = pygame.sprite.spritecollideany(bomb, fruit_sprites)
  if fruit:
    make_explosion(fruit.x, fruit.y)
    fruit.reset()

  # Check collision player and bomb
  if pygame.sprite.collide_rect(player, bomb):
    running = False

  # Animate the explosions
  for explosion in explosion_sprites:
    explosion.render(screen)
    if explosion.playing == False: 
      explosion.kill()

  # Update the window
  pygame.display.flip()

  # tick the clock!
  clock.tick(30)


# ---------------------------------------
# 1) Divide your code into modules 
# 2) Background color 
# 3) Add some clouds - Clouds move behind the other elements and gloat slowly from left to right. 
# 4) clouds can display one of three images and change their image each time they recycle. 
#    There are three cloud images to use. 
