import pygame
from gameobject import GameObject
from random import randint, choice
from constants import lanes


class Chicken(GameObject):
 def __init__(self):
   super(Chicken, self).__init__(0, 0, 'chicken(32x34).png')
   self.dx = (randint(0, 200) / 100) + 1
   self.dy = 0
   self.reset() # call reset here! 

 def move(self):
   self.x += self.dx
   self.y += self.dy
   # Check the y position of the Chicken
   if self.x > 500: 
     self.reset()
     
 def reset(self):
   self.x = -64
   self.y = choice(lanes)

 def render(self, screen):
   self.rect.x = self.x
   self.rect.y = self.y
   screen.blit(self.surf, (self.x, self.y))