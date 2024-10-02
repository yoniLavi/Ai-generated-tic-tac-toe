'''
This file contains the Game class that represents the tic-tac-toe game.
'''
class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.result = None
    def is_game_over(self):
        return self.game_over
    def get_current_player(self):
        return self.current_player
    def make_move(self, move):
        row, col = move
        self.board[row][col] = self.current_player
        self.check_game_over()
        # Switch to the other player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_game_over(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                self.game_over = True
                self.result = row[0] + " wins"
                return
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                self.game_over = True
                self.result = self.board[0][col] + " wins"
                return
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.game_over = True
            self.result = self.board[0][0] + " wins"
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.game_over = True
            self.result = self.board[0][2] + " wins"
            return
        # Check for a tie
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
            self.game_over = True
            self.result = "Tie"
    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += " | ".join(row) + "\n"
            board_str += "---------\n"
        return board_str
    def get_result(self):
        return self.result