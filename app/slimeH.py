import pygame
from gameobject import GameObject
from random import randint, choice
from constants import lanes

class SlimeH(GameObject):
 def __init__(self):
   super(SlimeH, self).__init__(0, 0, 'slime1.png')
   self.dx = (randint(0, 200) / 100) + 1
   self.dy = 0
   self.reset() # call reset here! 

 def move(self):
   self.x += self.dx
   self.y += self.dy
   # Check the x position of the Slime
   if self.x > 500: 
     self.reset()
     
 def reset(self):
   self.x = -64
   self.y = choice(lanes)