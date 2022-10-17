import pygame

class Grid(pygame.sprite.Sprite):
  def __init__(self, screen):
    super().__init__()
    self.screen = screen