import pygame
from random import randint, choice
from GameObject import GameObject
from constants import lanes
from AnimatedObject import AnimatedObject
# -------------------------------------------
# Bomb


class Bomb(AnimatedObject):
  def __init__(self):
    bomb_anim = [
        ('images/bomb/bomb-1.png', 20),
        ('images/bomb/bomb-2.png', 3),
        ('images/bomb/bomb-3.png', 3),
        ('images/bomb/bomb-4.png', 3),
        ('images/bomb/bomb-5.png', 10),
        ('images/bomb/bomb-4.png', 3),
        ('images/bomb/bomb-3.png', 3),
        ('images/bomb/bomb-2.png', 3),
        ('images/bomb/bomb-1.png', 13),
        ('images/bomb/bomb-6.png', 5),
        ('images/bomb/bomb-7.png', 15),
        ('images/bomb/bomb-6.png', 3),
        ('images/bomb/bomb-1.png', 3),
        ('images/bomb/bomb-8.png', 3),
        ('images/bomb/bomb-9.png', 23),
        ('images/bomb/bomb-8.png', 3),
        ('images/bomb/bomb-1.png', 13),
    ]
    super(Bomb, self).__init__(0, 0, bomb_anim)
    self.dx = 0
    self.dy = 0
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x > 500 or self.x < -64 or self.y > 500 or self.y < -64:
      self.reset()

  def reset(self):
    direction = randint(1, 4)
    if direction == 1: # left
      self.x = -64
      self.y = choice(lanes)
      self.dx = (randint(0, 200) / 100) + 1
      self.dy = 0
    elif direction == 2: # right
      self.x = 500
      self.y = choice(lanes)
      self.dx = ((randint(0, 200) / 100) + 1) * -1
      self.dy = 0
    elif direction == 3: # down
      self.x = choice(lanes)
      self.y = -64
      self.dx = 0
      self.dy = (randint(0, 200) / 100) + 1
    else:
      self.x = choice(lanes)
      self.y = 500
      self.dx = 0
      self.dy = ((randint(0, 200) / 100) + 1) * -1

