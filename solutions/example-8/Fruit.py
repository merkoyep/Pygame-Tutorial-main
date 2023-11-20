import pygame
from random import randint, choice
from constants import lanes
from GameObject import GameObject

# ----------------------------------------------
# Fruit

class Fruit(GameObject):
  def __init__(self):
    super(Fruit, self).__init__(0, 0, 'images/strawberry.png')
    self.surfs = [
      pygame.image.load("images/lemon.png"),
      pygame.image.load("images/apple.png"),
      pygame.image.load("images/strawberry.png")
    ]
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = 0
    self.flavor = "swwet"
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x > 500:
      self.reset()

  def reset(self):
    n = randint(0, 2)
    self.surf = self.surfs[n]
    if n == 0:
      self.flavor = "sour"
    else: 
      self.flavor = "sweet"
    self.x = -64
    self.y = choice(lanes)

