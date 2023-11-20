import pygame
from random import randint, choice
from GameObject import GameObject
from constants import lanes

# ----------------------------------------------
# Apple

class PointsSprite(pygame.sprite.Sprite):
  def __init__(self, x, y, score):
    super(PointsSprite, self).__init__()
    self.font = pygame.font.SysFont('Comic Sans MS', 30)
    self.surf = self.font.render(f"{score}", False, (0, 0, 0))
    self.dx = 0
    self.dy = -2
    self.x = x
    self.y = y
    self.timer = 50
    # self.rect = self.surf.get_rect()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    self.timer -= 1
    self.surf.set_alpha(255 * self.timer / 100)
    if self.timer < 0:
      self.reset()

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

  def reset(self):
    self.kill()