"""
This file contains the Player classes.
"""
import random
import math


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
        board = game.get_board()
        best_score = -math.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = game.get_current_player()
                    score = self._minimax(game, board, 0, False, -math.inf, math.inf)
                    board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def _minimax(self, game, board, depth, is_maximizing, alpha, beta):
        result = self._check_winner(board)
        if result is not None:
            return self._get_score(game, result, depth)

        if is_maximizing:
            best_score = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = game.get_current_player()
                        score = self._minimax(game, board, depth + 1, False, alpha, beta)
                        board[i][j] = " "
                        best_score = max(score, best_score)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = 'O' if game.get_current_player() == 'X' else 'X'
                        score = self._minimax(game, board, depth + 1, True, alpha, beta)
                        board[i][j] = " "
                        best_score = min(score, best_score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score

    def _check_winner(self, board):
        # Check rows, columns, and diagonals
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != " ":
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != " ":
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]
        
        # Check for a tie
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            return "tie"
        
        return None

    def _get_score(self, game, result, depth):
        if result == "tie":
            return 0
        elif result == game.get_current_player():
            return 10 - depth
        else:
            return depth - 10
