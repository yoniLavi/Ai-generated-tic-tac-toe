"""
This is the main file that runs the tic-tac-toe game.
"""
import argparse
from game import Game
from player import HumanPlayer, AIPlayer


def print_board(board):
    """
    Print the game board.

    Args:
        board (list): A 2D list representing the game board.
    """
    for i, row in enumerate(board):
        print(" | ".join(cell if cell != " " else str(i*3 + j + 1) for j, cell in enumerate(row)))
        if i < 2:
            print("---------")


def play_game(game, player1, player2):
    """
    Play a game of Tic-Tac-Toe.

    Args:
        game (Game): The game instance.
        player1 (Player): The first player (X).
        player2 (Player): The second player (O).
    """
    players = {
        "X": player1,
        "O": player2
    }

    while not game.is_game_over():
        print_board(game.get_board())
        current_player = game.get_current_player()
        print(f"Current player: {current_player}")

        move = players[current_player].get_move(game)
        game.make_move(move)

    print_board(game.get_board())
    print("Game Over!")
    print("Result:", game.get_result())


def main():
    """
    The main function to set up and run the Tic-Tac-Toe game.
    """
    game = Game()
    human_player = HumanPlayer()
    ai_player = AIPlayer()

    print("Welcome to Tic-Tac-Toe!")
    print("You'll be playing against an AI opponent.")
    
    while True:
        try:
            difficulty = int(input("Select AI difficulty (1: Easy, 2: Medium, 3: Hard): "))
            if 1 <= difficulty <= 3:
                ai_player.set_strength_level(difficulty)
                break
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nYou're playing against AI level {difficulty}. Good luck!")

    play_game(game, human_player, ai_player)


if __name__ == "__main__":
    main()
