import pygame
from cell import Cell

class Game:
  def __init__(self, screen) -> None:
    self.screen = screen

  def run(self):
    cells = []
    for i in range(9):
      for j in range(9):
        cells.append(Cell(self.screen, i, j))
    cells = pygame.sprite.Group(cells).draw(self.screen)
      
