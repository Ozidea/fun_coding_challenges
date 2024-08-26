import pygame

class Board:
    def __init__(self, width, height, grid_size):
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.grid_width = width // grid_size
        self.grid_height = height // grid_size
        self.grid = [[0 for _ in range(self.grid_height)] for _ in range(self.grid_width)]

    def reset(self):
        self.grid = [[0 for _ in range(self.grid_height)] for _ in range(self.grid_width)]

    def draw(self, screen):
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                color = (0, 0, 0) if self.grid[x][y] == 1 else (255, 255, 255)
                pygame.draw.rect(screen, color, (x * self.grid_size, y * self.grid_size, self.grid_size, self.grid_size))

    def get_cell(self, x, y):
        return self.grid[x][y]

    def set_cell(self, x, y, value):
        self.grid[x][y] = value
