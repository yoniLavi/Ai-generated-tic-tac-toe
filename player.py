"""
This file contains the Player classes.
"""
import random

class Player:
    def get_move(self, game):
        raise NotImplementedError("Subclasses must implement get_move method")

class HumanPlayer(Player):
    def get_move(self, game):
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
    def __init__(self):
        self.strength_level = 1

    def set_strength_level(self, level):
        self.strength_level = level

    def get_move(self, game):
        if self.strength_level == 1:
            return self._get_hard_move(game)
        elif self.strength_level == 2:
            return self._get_medium_move(game)
        else:
            return self._get_easy_move(game)

    def _get_easy_move(self, game):
        return self._get_random_move(game)

    def _get_medium_move(self, game):
        if random.random() < 0.7:  # Increased probability of smart move
            return self._get_smart_move(game)
        else:
            return self._get_random_move(game)

    def _get_hard_move(self, game):
        board = game.get_board()
        player = game.get_current_player()
        opponent = 'O' if player == 'X' else 'X'

        # Check for winning move
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    if self._check_winner(board) == player:
                        board[i][j] = " "
                        return (i, j)
                    board[i][j] = " "

        # Check for blocking opponent's winning move
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = opponent
                    if self._check_winner(board) == opponent:
                        board[i][j] = " "
                        return (i, j)
                    board[i][j] = " "

        # If no immediate winning or blocking move, use minimax
        best_score, best_move = self._minimax(game, 0, True, float('-inf'), float('inf'))
        return best_move

    def _get_random_move(self, game):
        board = game.get_board()
        available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
        return random.choice(available_moves)

    def _get_smart_move(self, game):
        board = game.get_board()
        player = game.get_current_player()
        opponent = 'O' if player == 'X' else 'X'

        # Check for winning move
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    if self._check_winner(board) == player:
                        board[i][j] = " "
                        return (i, j)
                    board[i][j] = " "

        # Check for blocking opponent's winning move
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = opponent
                    if self._check_winner(board) == opponent:
                        board[i][j] = " "
                        return (i, j)
                    board[i][j] = " "

        # Choose center if available
        if board[1][1] == " ":
            return (1, 1)

        # Choose a corner
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        available_corners = [corner for corner in corners if board[corner[0]][corner[1]] == " "]
        if available_corners:
            return random.choice(available_corners)

        # Choose any available edge
        edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
        available_edges = [edge for edge in edges if board[edge[0]][edge[1]] == " "]
        if available_edges:
            return random.choice(available_edges)

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
        return None

    def _minimax(self, game, depth, is_maximizing, alpha, beta):
        if game.is_game_over():
            result = game.get_result()
            if result == "X wins":
                return 10 - depth, None
            elif result == "O wins":
                return depth - 10, None
            else:
                return 0, None

        if is_maximizing:
            best_score = float('-inf')
            best_move = None
            for i in range(3):
                for j in range(3):
                    if game.get_board()[i][j] == " ":
                        game.make_move((i, j))
                        score, _ = self._minimax(game, depth + 1, False, alpha, beta)
                        game.undo_move((i, j))
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score, best_move
        else:
            best_score = float('inf')
            best_move = None
            for i in range(3):
                for j in range(3):
                    if game.get_board()[i][j] == " ":
                        game.make_move((i, j))
                        score, _ = self._minimax(game, depth + 1, True, alpha, beta)
                        game.undo_move((i, j))
                        if score < best_score:
                            best_score = score
                            best_move = (i, j)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score, best_move
