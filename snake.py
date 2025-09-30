import pygame
from constants import *

class Snake:
    def __init__(self, x=GRID_WIDTH // 2, y=GRID_HEIGHT // 2):
        """Initialize the snake at the center of the screen"""
        self.body = [(x, y)]
        self.direction = RIGHT
        self.grow_pending = 0
        
        # Add initial body segments
        for i in range(1, INITIAL_SNAKE_LENGTH):
            self.body.append((x - i, y))
    
    def move(self):
        """Move the snake in the current direction"""
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Add new head
        self.body.insert(0, new_head)
        
        # Remove tail unless growing
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()
    
    def change_direction(self, new_direction):
        """Change the snake's direction, but prevent 180-degree turns"""
        # Prevent moving directly opposite to current direction
        opposite_directions = {
            UP: DOWN,
            DOWN: UP,
            LEFT: RIGHT,
            RIGHT: LEFT
        }
        
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction
    
    def grow(self, segments=1):
        """Make the snake grow by the specified number of segments"""
        self.grow_pending += segments
    
    def check_collision(self):
        """Check if the snake has collided with itself or the walls"""
        head_x, head_y = self.body[0]
        
        # Check wall collision
        if (head_x < 0 or head_x >= GRID_WIDTH or 
            head_y < 0 or head_y >= GRID_HEIGHT):
            return True
        
        # Check self collision
        if (head_x, head_y) in self.body[1:]:
            return True
        
        return False
    
    def get_head_position(self):
        """Get the position of the snake's head"""
        return self.body[0]
    
    def draw(self, screen):
        """Draw the snake on the screen"""
        for i, (x, y) in enumerate(self.body):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            
            # Different color for head
            if i == 0:
                pygame.draw.rect(screen, SNAKE_HEAD_COLOR, rect)
                pygame.draw.rect(screen, WHITE, rect, 2)  # White border for head
            else:
                pygame.draw.rect(screen, SNAKE_COLOR, rect)
                pygame.draw.rect(screen, DARK_GREEN, rect, 1)  # Darker border for body
    
    def get_length(self):
        """Get the current length of the snake"""
        return len(self.body)