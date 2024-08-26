import pygame
import random
from ant import Ant  # Import the Ant class from the ant.py file

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000,1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Langton's Ant")
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_SIZE = 10
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 500

grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]

# Create an Ant instance
ant = Ant(x=GRID_WIDTH // 2, y=GRID_HEIGHT // 2, direction='N', grid_height=GRID_HEIGHT, grid_width=GRID_WIDTH)


def move_ant():
    if grid[ant.x][ant.y] == 0:
        ant.turn_right()
        grid[ant.x][ant.y] = 1
    else:
        ant.turn_left()
        grid[ant.x][ant.y] = 0

    ant.move_forward(distance=1)


def draw_grid():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            color = BLACK if grid[x][y] == 1 else WHITE
            pygame.draw.rect(screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


def handle_keys():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                # Reset the grid and the ant position if needed
                global grid
                grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
                ant.x, ant.y = GRID_WIDTH // 2, GRID_HEIGHT // 2
                ant.direction = 'N'


# Main loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    handle_keys()

    move_ant()
    draw_grid()
    ant.draw(screen, GRID_SIZE)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
