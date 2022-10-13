import pygame
from cell import Cell
from constants import NUMBER_OF_SIDE_CELLS

class Game:
  def __init__(self, screen) -> None:
    self.screen = screen

  def run(self):
    cells = []
    for i in range(NUMBER_OF_SIDE_CELLS):
      for j in range(NUMBER_OF_SIDE_CELLS):
        cells.append(Cell(self.screen, i, j))
    cells = pygame.sprite.Group(cells).draw(self.screen)
      
