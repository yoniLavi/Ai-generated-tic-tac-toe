# Tic-Tac-Toe Game User Manual

Welcome to the Tic-Tac-Toe game user manual! This manual will guide you through the installation process, explain the main functions of the game, and provide instructions on how to play.

## Installation

To install and run the Tic-Tac-Toe game, please follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: [python.org](https://www.python.org/downloads/)

2. Clone or download the game code from the repository: [tic-tac-toe-game](https://github.com/your-repository-link)

3. Open a terminal or command prompt and navigate to the directory where you downloaded the game code.

4. Create a virtual environment (optional but recommended) by running the following command:
   ```
   python -m venv env
   ```

5. Activate the virtual environment:
   - On Windows:
     ```
     env\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source env/bin/activate
     ```

6. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

7. You are now ready to play the Tic-Tac-Toe game!

## Main Functions

The Tic-Tac-Toe game has the following main functions:

- `main()`: This function starts the game loop and controls the flow of the game. It creates a new game instance, creates human and AI players, and allows players to make moves until the game is over.

- `Game()`: This class represents the tic-tac-toe game. It initializes the game board, keeps track of the current player, checks for a game over condition, and allows players to make moves.

- `HumanPlayer()`: This class represents a human player. It prompts the user for their move and validates the input.

- `AIPlayer()`: This class represents an AI player. It has a strength level that determines the AI's move. The strength level can be adjusted to make the AI player stronger or weaker.

## How to Play

To play the Tic-Tac-Toe game, follow these steps:

1. Open a terminal or command prompt and navigate to the directory where you downloaded the game code.

2. Activate the virtual environment (if you created one) by running the appropriate command (see step 5 of the installation process).

3. Start the game by running the following command:
   ```
   python main.py
   ```

4. The game will display an empty tic-tac-toe board. The board is represented by a 3x3 grid of cells.

5. The game will prompt the human player to enter their move. Enter the row number (0-2) and column number (0-2) of the cell where you want to place your mark (X).

6. The AI player will then make its move. The AI's move will be displayed on the board.

7. Repeat steps 5 and 6 until the game is over. The game can end in one of the following ways:
   - One player wins by getting three of their marks in a row, column, or diagonal.
   - The game board is full and there is no winner (tie).

8. After the game is over, the result will be displayed. If a player wins, their mark (X or O) will be shown. If the game ends in a tie, "Tie" will be displayed.

9. You can play the game again by running the `python main.py` command.

## Adjusting AI Strength Level

The AI player has a strength level that determines its move. By default, the strength level is set to 1. You can adjust the strength level to make the AI player stronger or weaker.

To adjust the AI strength level, follow these steps:

1. Open the `main.py` file in a text editor.

2. Locate the line that sets the AI strength level:
   ```
   ai_player.set_strength_level(2)
   ```

3. Change the number inside the parentheses to the desired strength level. For example, to set the strength level to 3, change the line to:
   ```
   ai_player.set_strength_level(3)
   ```

4. Save the file and run the game again. The AI player will now make moves based on the adjusted strength level.

## Conclusion

Congratulations! You have successfully installed and learned how to play the Tic-Tac-Toe game. Enjoy playing against the AI player and have fun! If you have any questions or need further assistance, please don't hesitate to contact us.