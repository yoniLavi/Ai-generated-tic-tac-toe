'''
This file contains the Player classes.
'''
class HumanPlayer:
    def get_move(self, game):
        while True:
            try:
                row = int(input("Enter the row (0-2): "))
                col = int(input("Enter the column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and game.board[row][col] == ' ':
                    return (row, col)
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")
class AIPlayer:
    def __init__(self):
        self.strength_level = 1
    def set_strength_level(self, level):
        self.strength_level = level
    def get_move(self, game):
        # AI logic to make a move based on the strength level
        # Implement your AI algorithm here
        # For now, let's just make a random move
        import random
        available_moves = [(i, j) for i in range(3) for j in range(3) if game.board[i][j] == ' ']
        return random.choice(available_moves)