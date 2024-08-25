import numpy as np
import pygame
from pygame.locals import *
import random

from Constants import Constants
from Colors import Color

class Board:
    def __init__(self, SCREEN):
        self.SCREEN = SCREEN
        self.block_count = Constants.block_count
        self.new_board = np.zeros((self.block_count, self.block_count), dtype=int)

    def create_random_color(self):
        return 0

    def create_out_of_nothing(self, x, y):
        a = random.randint(1, x)
        b = random.randint(1, y)
        return a - 1, b - 1

    def create_random_grid(self, ROW, COL):
        return np.random.randint(0, 2, (ROW, COL))

    def get_neighbors_sum(self, board, x, y):
        total = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:  # Skip the cell itself
                    total += board[(x + dx) % self.block_count][(y + dy) % self.block_count]
        return total

    def updateBoard(self, updated_board, progress, delete_all=False):
        for x in range(self.block_count):
            for y in range(self.block_count):
                total = self.get_neighbors_sum(updated_board, x, y)

                if progress:
                    if updated_board[x][y] == 1:
                        if total < 2 or total > 3:
                            self.new_board[x][y] = 0
                        else:
                            self.new_board[x][y] = 1
                    else:
                        if total == 3:
                            self.new_board[x][y] = 1
                else:
                    if delete_all:
                        self.new_board[x][y] = 0
                    else:
                        self.new_board[x][y] = updated_board[x][y]

                rect = pygame.Rect(y * Constants.SCALE_H, x * Constants.SCALE_W, Constants.SCALE_H, Constants.SCALE_W)
                if self.new_board[x][y] == 1:
                    pygame.draw.rect(self.SCREEN, (self.create_random_color(), self.create_random_color(), self.create_random_color()), rect)
                else:
                    color = Color().get_white() if not delete_all else Color().get_black()
                    pygame.draw.rect(self.SCREEN, color, rect)

        return self.new_board
