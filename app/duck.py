import pygame
from gameobject import GameObject
from random import randint, choice
from constants import lanes

class Duck(GameObject):
 def __init__(self):
   super(Duck, self).__init__(0, 0, 'duck(36x36).png')
   self.dx = 0
   self.dy = (randint(0, 200) / 100) + 1
   self.reset() # call reset here! 

 def move(self):
   self.x += self.dx
   self.y += self.dy
   # Check the y position of the duck
   if self.y > 500: 
     self.reset()
     
 def reset(self):
   self.x = choice(lanes)
   self.y = -64