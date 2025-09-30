import pygame
import random
from constants import *

class Food:
    def __init__(self):
        """Initialize food at a random position"""
        self.position = self.generate_position()
        self.eaten = False
    
    def generate_position(self, snake_body=None):
        """Generate a random position for food, avoiding snake body if provided"""
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            position = (x, y)
            
            # If snake body is provided, make sure food doesn't spawn on snake
            if snake_body is None or position not in snake_body:
                return position
    
    def respawn(self, snake_body=None):
        """Respawn food at a new random position"""
        self.position = self.generate_position(snake_body)
        self.eaten = False
    
    def check_eaten(self, snake_head_position):
        """Check if the food has been eaten by the snake"""
        if self.position == snake_head_position:
            self.eaten = True
            return True
        return False
    
    def draw(self, screen):
        """Draw the food on the screen"""
        if not self.eaten:
            x, y = self.position
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            
            # Draw food as a circle
            center_x = x * GRID_SIZE + GRID_SIZE // 2
            center_y = y * GRID_SIZE + GRID_SIZE // 2
            radius = GRID_SIZE // 2 - 2
            
            pygame.draw.circle(screen, FOOD_COLOR, (center_x, center_y), radius)
            pygame.draw.circle(screen, WHITE, (center_x, center_y), radius, 2)  # White border
    
    def get_position(self):
        """Get the current position of the food"""
        return self.position