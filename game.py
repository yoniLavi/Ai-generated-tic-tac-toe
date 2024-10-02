"""
This file contains the Game class that represents the tic-tac-toe game.
"""


class Game:
    """
    Represents a Tic-Tac-Toe game.
    """

    def __init__(self):
        """
        Initialize a new game with an empty board and 'X' as the starting player.
        """
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.result = None

    def is_game_over(self):
        """
        Check if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.game_over

    def get_current_player(self):
        """
        Get the current player.

        Returns:
            str: The current player ('X' or 'O').
        """
        return self.current_player

    def get_board(self):
        """
        Get the current game board.

        Returns:
            list: A 2D list representing the game board.
        """
        return self.board

    def make_move(self, move):
        """
        Make a move on the board.

        Args:
            move (tuple): A tuple containing the row and column of the move.

        Raises:
            ValueError: If the move is invalid.
        """
        row, col = move
        if not (0 <= row < 3 and 0 <= col < 3):
            raise ValueError("Invalid move: Position out of bounds")
        if self.board[row][col] != " ":
            raise ValueError("Invalid move: This position is already occupied")
        self.board[row][col] = self.current_player
        self._check_game_over()
        self._switch_player()

    def undo_move(self, move):
        """
        Undo a move on the board.

        Args:
            move (tuple): A tuple containing the row and column of the move to undo.
        """
        row, col = move
        self.board[row][col] = " "
        self._switch_player()
        self.result = None
        self.game_over = False

    def _switch_player(self):
        """
        Switch to the other player.
        """
        self.current_player = "O" if self.current_player == "X" else "X"

    def _check_game_over(self):
        """
        Check if the game is over and update the game state accordingly.
        """
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                self._end_game(row[0] + " wins")
                return

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                self._end_game(self.board[0][col] + " wins")
                return

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self._end_game(self.board[0][0] + " wins")
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            self._end_game(self.board[0][2] + " wins")
            return

        # Check for a tie
        if all(self.board[i][j] != " " for i in range(3) for j in range(3)):
            self._end_game("Tie")

    def _end_game(self, result):
        """
        End the game with the given result.

        Args:
            result (str): The result of the game.
        """
        self.game_over = True
        self.result = result

    def get_result(self):
        """
        Get the result of the game.

        Returns:
            str: The result of the game, or None if the game is not over.
        """
        return self.result
