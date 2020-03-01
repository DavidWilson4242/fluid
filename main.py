import pygame
import math
from fluid import Fluid

class GameState:
  def __init__(self):
    self.fluid = Fluid(0, 0)

  def runGame(self):
    pass

if __name__ == "__main__":
  game = GameState()
  game.runGame()
