import pygame


class Ant:
    def __init__(self, x=0, y=0, direction='N', grid_height=1, grid_width=1):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid_height = grid_height
        self.grid_width = grid_width

    def __str__(self):
        return f"Ant(x={self.x}, y={self.y}, direction='{self.direction}')"

    def move_forward(self,distance=1,):
        if self.direction == 'N':
            self.y += distance
        elif self.direction == 'S':
            self.y -= distance
        elif self.direction == 'E':
            self.x += distance
        elif self.direction == 'W':
            self.x -= distance
        else:
            raise ValueError("Invalid direction. Use 'N', 'E', 'S', or 'W'.")
        self.x %= self.grid_width
        self.y %= self.grid_height
    def turn_left(self):
        """
        Turn the ant 90 degrees to the left.
        """
        direction_order = ['N', 'W', 'S', 'E']
        current_index = direction_order.index(self.direction)
        new_index = (current_index + 1) % 4
        self.direction = direction_order[new_index]

    def turn_right(self):
        """
        Turn the ant 90 degrees to the right.
        """
        direction_order = ['N', 'E', 'S', 'W']
        current_index = direction_order.index(self.direction)
        new_index = (current_index + 1) % 4
        self.direction = direction_order[new_index]
    def draw(self, screen, grid_size):
        # Calculate the center of the ant
        ant_center_x = self.x * grid_size + grid_size // 2
        ant_center_y = self.y * grid_size + grid_size // 2
        # Define the radius of the circle
        radius = 3
        # Draw the circle on the screen
        pygame.draw.circle(screen, (255, 0, 0), (ant_center_x, ant_center_y), radius)