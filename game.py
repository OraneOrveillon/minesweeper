from lib2to3.pgen2.token import NUMBER
import pygame
import random
from cell import Cell
from constants import NUMBER_OF_SIDE_CELLS, NUMBER_OF_MINES
from cell import MinedCell

class Game:
  def __init__(self, screen) -> None:
    self.screen = screen

  def run(self):
    cells = []
    mines_coords = []
    for i in range (NUMBER_OF_MINES):
      # Same as `do (new mine coords) while (same coords)`
      while True:
        mine_coords = (random.randint(0, NUMBER_OF_SIDE_CELLS), random.randint(0, NUMBER_OF_SIDE_CELLS))
        if not self.mines_coords.__contains__(mine_coords): break
      self.mines_coords.append(mine_coords) 

    print(self.mines_coords)


    for i in range(NUMBER_OF_SIDE_CELLS):
      for j in range(NUMBER_OF_SIDE_CELLS):
        if self.mines_coords.__contains__((i, j)):
          self.cells.append(MinedCell(self.screen, i, j))
        else: 
          self.cells.append(Cell(self.screen, i, j))

  def run(self):
    pygame.sprite.Group(self.cells).draw(self.screen)
      
