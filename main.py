"""
This is the main file that runs the tic-tac-toe game.
"""
from game import Game
from player import HumanPlayer, AIPlayer


def print_board(board):
    """
    Print the game board.

    Args:
        board (list): A 2D list representing the game board.
    """
    for row in board:
        print(" | ".join(row))
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

    ai_player.set_strength_level(2)  # Set the strength level to 2 (can be adjusted)

    play_game(game, human_player, ai_player)


if __name__ == "__main__":
    main()
