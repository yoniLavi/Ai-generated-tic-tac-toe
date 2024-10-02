# Tic-Tac-Toe Game

This is a Python implementation of the classic Tic-Tac-Toe game, featuring a command-line interface and an AI opponent with adjustable difficulty levels.

## Features

- Play Tic-Tac-Toe against an AI opponent
- Adjustable AI difficulty levels
- Command-line interface
- Undo move functionality
- Game state tracking and result reporting

## Installation

1. Ensure you have Python 3.6 or higher installed on your system.
2. Clone this repository:
   ```
   git clone https://github.com/your-username/tic-tac-toe-game.git
   cd tic-tac-toe-game
   ```
3. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## How to Play

1. Run the game:
   ```
   python main.py
   ```
2. The game will display an empty 3x3 board.
3. When prompted, enter your move by specifying a number from 1 to 9, corresponding to the board positions:
   ```
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```
4. The AI will then make its move.
5. Continue playing until the game ends (win, lose, or tie).

## AI Difficulty Levels

The AI player has different strength levels:

1. Easy: Makes random moves
2. Medium: Combines random moves with some strategic choices
3. Hard: Uses the minimax algorithm for optimal play

To change the AI difficulty, modify the `set_strength_level()` call in the `main()` function of `main.py`:

```python
ai_player.set_strength_level(2)  # 1 for Easy, 2 for Medium, 3 for Hard
```

## Project Structure

- `main.py`: Contains the main game loop and user interface
- `game.py`: Implements the `Game` class, which manages the game state
- `player.py`: Defines the `Player`, `HumanPlayer`, and `AIPlayer` classes
- `test_game_basics.py`, `test_tic_tac_toe.py`, `test_ai_player.py`: Unit tests for the game components

## Running Tests

To run the unit tests, execute:

```
python -m unittest discover
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
