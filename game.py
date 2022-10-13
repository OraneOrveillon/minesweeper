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
      while True:
        mine_coords = (random.randint(0, NUMBER_OF_SIDE_CELLS), random.randint(0, NUMBER_OF_SIDE_CELLS))
        if not mines_coords.__contains__(mine_coords): break
      mines_coords.append(mine_coords) 


    for i in range(NUMBER_OF_SIDE_CELLS):
      for j in range(NUMBER_OF_SIDE_CELLS):
        if mines_coords.__contains__((i, j)):
          cells.append(MinedCell(self.screen, i, j))
        else: 
          cells.append(Cell(self.screen, i, j))
    cells = pygame.sprite.Group(cells).draw(self.screen)
      
