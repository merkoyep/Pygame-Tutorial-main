import pygame
from gameobject import GameObject
from random import randint, choice
from constants import lanes

class SlimeV(GameObject):
 def __init__(self):
   super(SlimeV, self).__init__(0, 0, 'slime2.png')
   self.dx = 0
   self.dy = (randint(0, 200) / 100) + 1
   self.reset() # call reset here! 

 def move(self):
   self.x += self.dx
   self.y += self.dy
   # Check the y position of the slime
   if self.y > 500: 
     self.reset()
     
 def reset(self):
   self.x = choice(lanes)
   self.y = -64
