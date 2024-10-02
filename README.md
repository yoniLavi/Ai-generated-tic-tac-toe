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

1. Run the game with optional command-line arguments:
   ```
   python main.py [-d DIFFICULTY] [-p PLAYER]
   ```
   - `-d` or `--difficulty`: Set AI difficulty level (1: Easy, 2: Medium, 3: Hard). Default is 2 (Medium).
   - `-p` or `--player`: Choose player symbol (X or O). Default is X.

   Example: `python main.py -d 3 -p O` to play as O against Hard AI.

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

You can set the AI difficulty using the `-d` or `--difficulty` command-line argument when starting the game.

## Project Structure

- `main.py`: Contains the main game loop and user interface
- `game.py`: Implements the `Game` class, which manages the game state
- `player.py`: Defines the `Player`, `HumanPlayer`, and `AIPlayer` classes
- `test_game_basics.py`, `test_tic_tac_toe.py`, `test_ai_player.py`: Unit tests for the game components

## Running Tests

There are two ways to run the tests:

1. Using the `run_tests.py` script:
   ```
   python run_tests.py
   ```
   This will discover and run all tests in the project.

2. Using the unittest module directly:
   ```
   python -m unittest discover
   ```

Both methods will run all the tests in the project, including:
- `test_game_basics.py`
- `test_tic_tac_toe.py`
- `test_ai_player.py`

The `run_tests.py` script provides a convenient way to run all tests with a single command and displays detailed output for each test.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
