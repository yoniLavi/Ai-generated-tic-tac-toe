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
                move = int(input("Enter your move (1-9): "))
                if 1 <= move <= 9:
                    row, col = divmod(move - 1, 3)
                    if board[row][col] == " ":
                        return (row, col)
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
        if self.strength_level == 1:
            return self._get_random_move(game)
        elif self.strength_level == 2:
            return self._get_medium_move(game)
        else:
            return self._get_hard_move(game)

    def _get_random_move(self, game):
        board = game.get_board()
        available_moves = [
            (i, j) for i in range(3) for j in range(3) if board[i][j] == " "
        ]
        return random.choice(available_moves)

    def _get_medium_move(self, game):
        # Implement a medium difficulty AI strategy
        # For now, it's the same as random
        return self._get_random_move(game)

    def _get_hard_move(self, game):
        # Implement a hard difficulty AI strategy
        # For now, it's the same as random
        return self._get_random_move(game)
