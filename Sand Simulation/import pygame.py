import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sand Falling Simulation")

# Colors
BLACK = (255,255,255)
SAND_COLOR = (194, 178, 128)

# Sand particle size
SAND_SIZE = 10  # Size of each sand particle

# Adjusted grid dimensions to match the sand size
GRID_WIDTH = WIDTH // SAND_SIZE
GRID_HEIGHT = HEIGHT // SAND_SIZE

DIRECTION = ["Left","Right"]
FPS = 120

# Sand grid (2D array)
sand_grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]

def reset_sand_grid():
    global sand_grid
    sand_grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]


def draw_sand():
    """Draws the sand particles on the screen."""
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if sand_grid[x][y] == 1:
                pygame.draw.rect(screen, SAND_COLOR, (x * SAND_SIZE, y * SAND_SIZE, SAND_SIZE, SAND_SIZE))


def update_sand():
    """Updates the sand particles to simulate falling with random direction."""
    for y in range(GRID_HEIGHT-2, -1, -1):  # Start from the bottom second row and go up
        for x in range(GRID_WIDTH):
            if sand_grid[x][y] == 1:
                # Move down if the space below is empty
                if sand_grid[x][y + 1] == 0:
                    sand_grid[x][y] = 0
                    sand_grid[x][y + 1] = 1
                else:
                    # Randomly choose left (-1) or right (1) direction
                    direction = random.choice(DIRECTION)

                    # Try to move in the chosen direction
                    if direction == "Left" and x > 0 and sand_grid[x - 1][y + 1] == 0:
                        sand_grid[x][y] = 0
                        sand_grid[x - 1][y + 1] = 1
                    elif direction == "Right" and x < GRID_WIDTH - 1 and sand_grid[x + 1][y + 1] == 0:
                        sand_grid[x][y] = 0
                        sand_grid[x + 1][y + 1] = 1


def add_sand(mouse_x, mouse_y):
    """Adds sand particles at the given location."""
    grid_x = mouse_x // SAND_SIZE
    grid_y = mouse_y // SAND_SIZE
    if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
        sand_grid[grid_x][grid_y] = 1

def remove_sand(mouse_x, mouse_y):
    """Adds sand particles at the given location."""
    grid_x = mouse_x // SAND_SIZE
    grid_y = mouse_y // SAND_SIZE
    if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
        sand_grid[grid_x][grid_y] = 0

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                # Reset the sand grid
                sand_grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
            

    # Get mouse position and add sand if mouse is pressed
    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        add_sand(mouse_x, mouse_y)
    elif pygame.mouse.get_pressed()[2]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        remove_sand(mouse_x, mouse_y)

    update_sand()
    draw_sand()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
