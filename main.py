#!/usr/bin/env python3
"""
Slither - A Snake-like Game
===========================

A classic Snake game implementation using Python and Pygame.

Controls:
- WASD or Arrow Keys: Move the snake
- P: Pause/Resume the game
- R: Restart game (when game over)
- Q: Quit game (when game over)

Author: AI Assistant
Date: September 30, 2025
"""

from game import Game

def main():
    """Main entry point for the Slither game"""
    try:
        print("Starting Slither - Snake Game...")
        print("Controls:")
        print("  WASD or Arrow Keys: Move")
        print("  P: Pause/Resume")
        print("  R: Restart (when game over)")
        print("  Q: Quit (when game over)")
        print("\nClose this window or press Ctrl+C to exit.")
        
        # Create and run the game
        game = Game()
        game.run()
        
    except KeyboardInterrupt:
        print("\nGame interrupted by user. Thanks for playing!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure you have pygame installed: pip install pygame")
    finally:
        print("Game ended. Thanks for playing Slither!")

if __name__ == "__main__":
    main()