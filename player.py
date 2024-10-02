"""
This file contains the Player classes.
"""
import random


class Player:
    """
    Base class for all players.
    """

    def get_move(self, game):
        """
        Get the player's move.

        Args:
            game (Game): The current game state.

        Returns:
            tuple: A tuple containing the row and column of the move.
        """
        raise NotImplementedError("Subclasses must implement get_move method")


class HumanPlayer(Player):
    """
    Represents a human player.
    """

    def get_move(self, game):
        """
        Get the human player's move through user input.

        Args:
            game (Game): The current game state.

        Returns:
            tuple: A tuple containing the row and column of the move.
        """
        board = game.get_board()
        while True:
            try:
                row = int(input("Enter the row (0-2): "))
                col = int(input("Enter the column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    return (row, col)
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")


class AIPlayer(Player):
    """
    Represents an AI player.
    """

    def __init__(self):
        """
        Initialize the AI player with a default strength level.
        """
        self.strength_level = 1

    def set_strength_level(self, level):
        """
        Set the strength level of the AI player.

        Args:
            level (int): The strength level of the AI.
        """
        self.strength_level = level

    def get_move(self, game):
        """
        Get the AI player's move based on the current game state.

        Args:
            game (Game): The current game state.

        Returns:
            tuple: A tuple containing the row and column of the move.
        """
        # AI logic to make a move based on the strength level
        # Implement your AI algorithm here
        # For now, let's just make a random move
        board = game.get_board()
        available_moves = [
            (i, j) for i in range(3) for j in range(3) if board[i][j] == " "
        ]
        return random.choice(available_moves)
