import pygame
import sys
from constants import *
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Slither - Snake Game")
        self.clock = pygame.time.Clock()
        
        # Game state
        self.running = True
        self.game_over = False
        self.paused = False
        self.score = 0
        self.speed = INITIAL_SPEED
        
        # Game objects
        self.snake = Snake()
        self.food = Food()
        
        # Make sure food doesn't spawn on snake initially
        self.food.respawn(self.snake.body)
        
        # Font for text rendering
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
    
    def handle_events(self):
        """Handle all game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_r:
                        self.restart_game()
                    elif event.key == pygame.K_q:
                        self.running = False
                
                elif event.key == pygame.K_p:
                    self.paused = not self.paused
                
                elif not self.paused:
                    # Snake movement controls
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.snake.change_direction(RIGHT)
    
    def update(self):
        """Update game state"""
        if self.game_over or self.paused:
            return
        
        # Move snake
        self.snake.move()
        
        # Check collisions
        if self.snake.check_collision():
            self.game_over = True
            return
        
        # Check if food is eaten
        if self.food.check_eaten(self.snake.get_head_position()):
            self.score += FOOD_SCORE
            self.snake.grow()
            self.food.respawn(self.snake.body)
            
            # Increase speed slightly as score increases
            if self.score % 50 == 0 and self.speed < MAX_SPEED:
                self.speed += SPEED_INCREMENT
    
    def draw(self):
        """Draw everything on the screen"""
        # Clear screen
        self.screen.fill(BLACK)
        
        # Draw grid (optional, for visual appeal)
        self.draw_grid()
        
        # Draw game objects
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        
        # Draw UI
        self.draw_ui()
        
        # Draw game over or pause screen
        if self.game_over:
            self.draw_game_over()
        elif self.paused:
            self.draw_pause_screen()
        
        pygame.display.flip()
    
    def draw_grid(self):
        """Draw a subtle grid for visual appeal"""
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, (20, 20, 20), (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, (20, 20, 20), (0, y), (SCREEN_WIDTH, y))
    
    def draw_ui(self):
        """Draw the user interface (score, length, speed)"""
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        length_text = self.font.render(f"Length: {self.snake.get_length()}", True, WHITE)
        speed_text = self.font.render(f"Speed: {self.speed}", True, WHITE)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(length_text, (10, 50))
        self.screen.blit(speed_text, (10, 90))
        
        # Controls hint
        controls_text = pygame.font.Font(None, 24).render("WASD/Arrow Keys: Move | P: Pause", True, WHITE)
        self.screen.blit(controls_text, (SCREEN_WIDTH - 300, 10))
    
    def draw_game_over(self):
        """Draw game over screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        game_over_text = self.big_font.render("GAME OVER", True, RED)
        final_score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        restart_text = self.font.render("Press R to Restart or Q to Quit", True, WHITE)
        
        # Center the text
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        
        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(final_score_text, score_rect)
        self.screen.blit(restart_text, restart_rect)
    
    def draw_pause_screen(self):
        """Draw pause screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Pause text
        pause_text = self.big_font.render("PAUSED", True, YELLOW)
        resume_text = self.font.render("Press P to Resume", True, WHITE)
        
        # Center the text
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 25))
        resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25))
        
        self.screen.blit(pause_text, pause_rect)
        self.screen.blit(resume_text, resume_rect)
    
    def restart_game(self):
        """Restart the game"""
        self.game_over = False
        self.paused = False
        self.score = 0
        self.speed = INITIAL_SPEED
        self.snake = Snake()
        self.food = Food()
        self.food.respawn(self.snake.body)
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.speed)
        
        pygame.quit()
        sys.exit()