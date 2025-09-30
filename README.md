# Slither - Snake Game 🐍

A classic Snake game clone built with Python and Pygame. Guide your snake to eat food, grow longer, and avoid collisions!

## Features

- **Classic Snake Gameplay**: Move your snake around the grid to collect food
- **Dynamic Speed**: Game speed increases as your score grows
- **Smooth Controls**: Responsive WASD or arrow key controls
- **Visual Polish**: Clean graphics with grid lines and colored snake segments
- **Game States**: Pause functionality and game over screen with restart option
- **Score Tracking**: Keep track of your score and snake length

## Installation

### Prerequisites
- **Python 3.7 or higher** installed on your system

### Option 1: Using Virtual Environment (Recommended)

1. **Create a virtual environment**:
   ```bash
   python -m venv slither-env
   ```

2. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     slither-env\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source slither-env/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the game**:
   ```bash
   python main.py
   ```

5. **Deactivate when done** (optional):
   ```bash
   deactivate
   ```

### Option 2: Global Installation

1. **Install Pygame directly**:
   ```bash
   pip install -r requirements.txt
   ```
   Or manually:
   ```bash
   pip install pygame
   ```

2. **Run the game**:
   ```bash
   python main.py
   ```

> **Note**: Using a virtual environment is recommended to avoid conflicts with other Python projects and keep dependencies isolated.

## How to Play

1. **Start the game**:
   ```bash
   python main.py
   ```

2. **Controls**:
   - **WASD** or **Arrow Keys**: Move the snake
   - **P**: Pause/Resume the game
   - **R**: Restart game (when game over)
   - **Q**: Quit game (when game over)

3. **Objective**:
   - Eat the red food circles to grow your snake
   - Avoid hitting the walls or your own body
   - Try to achieve the highest score possible!

## Game Mechanics

- **Starting Length**: 3 segments
- **Growth**: Snake grows by 1 segment per food eaten
- **Speed**: Increases every 50 points (max speed: 20 FPS)
- **Scoring**: 10 points per food item
- **Collision**: Game ends if snake hits walls or itself

## File Structure

```
slither/
├── main.py          # Game entry point
├── game.py          # Main game engine and loop
├── snake.py         # Snake class with movement and collision
├── food.py          # Food class for random food generation
├── constants.py     # Game constants and configuration
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Customization

You can easily customize the game by modifying values in `constants.py`:

- **Screen size**: `SCREEN_WIDTH`, `SCREEN_HEIGHT`
- **Grid size**: `GRID_SIZE`
- **Colors**: Various color constants
- **Speed settings**: `INITIAL_SPEED`, `MAX_SPEED`
- **Snake settings**: `INITIAL_SNAKE_LENGTH`

## Screenshots

The game features:
- Green snake with darker green head and body segments
- Red circular food items
- Black background with subtle grid lines
- Real-time score, length, and speed display
- Pause and game over overlays

## Contributing

Feel free to fork this project and add your own features! Some ideas:
- High score persistence
- Different food types with varying points
- Power-ups and obstacles
- Multiple difficulty levels
- Sound effects and music

## License

This project is open source and available under the MIT License.

---

**Enjoy playing Slither!** 🎮
