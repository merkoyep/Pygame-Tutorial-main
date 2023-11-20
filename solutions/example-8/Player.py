from random import randint
import pygame
from constants import lanes
from AnimatedObject import AnimatedObject

# -------------------------------------------
# Player

# ---------------------------------------
# AnimatedObject test

class Player(AnimatedObject):
  def __init__(self):
    player_anim = [
        ('images/pink/pink-1.png', 10),
        ('images/pink/pink-2.png', 10),
        ('images/pink/pink-3.png', 10),
        ('images/pink/pink-1.png', 5),
        ('images/pink/pink-4.png', 5),
        ('images/pink/pink-5.png', 5)
    ]
    super(Player, self).__init__(0, 0, player_anim)
    self.dx = 0
    self.dy = 0
    self.pos_x = 1
    self.pos_y = 1
    self.state = 0
    self.reset()

  def left(self):
    if self.pos_x > 0:
      self.pos_x -= 1
    self.update_dx_dy()

  def right(self):
    if self.pos_x < len(lanes) - 1:
      self.pos_x += 1
    self.update_dx_dy()

  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
    self.update_dx_dy()

  def down(self):
    if self.pos_y < len(lanes) - 1:
      self.pos_y += 1
    self.update_dx_dy()

  def move(self):
    if self.state < 1:
      self.x -= (self.x - self.dx) * 0.25
      self.y -= (self.y - self.dy) * 0.25
    else:
      self.state -= 1

  def reset(self):
    self.x = lanes[self.pos_x]
    self.y = lanes[self.pos_y]
    self.dx = self.x
    self.dy = self.y
    self.state = 0
  
  def update_dx_dy(self):
    self.dx = lanes[self.pos_x]
    self.dy = lanes[self.pos_y]

  def stun(self):
    self.state = randint(15, 30)