import math
import pygame
from pygame.locals import *
import numpy as np
import random
from Conway import Conway
import Colors
from Board import Board
from Colors import Color
from Constants import Constants


def main():
    pygame.init()
    SCREEN = pygame.display.set_mode(Constants.SIZE)
    board = Board(SCREEN)
    pygame.display.set_caption("Conway's Game of Life")
    SCREEN.fill(Color().get_white())
    conway = Conway(board, SCREEN)
    conway.run_game(SCREEN)

    pygame.quit()

if __name__ == "__main__":
    main()
