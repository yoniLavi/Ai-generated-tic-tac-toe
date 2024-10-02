"""
This is the main file that runs the tic-tac-toe game.
"""
from game import Game
from player import HumanPlayer, AIPlayer

def main():
    # Create a new game instance
    game = Game()
    
    # Create human and AI players
    human_player = HumanPlayer()
    ai_player = AIPlayer()
    
    # Set the strength level of the AI player
    ai_player.set_strength_level(2)  # Set the strength level to 2 (can be adjusted)
    
    # Start the game loop
    while not game.is_game_over():
        # Print the current state of the game
        print(game)
        
        # Get the current player
        current_player = game.get_current_player()
        
        # Get the move based on the current player
        if current_player == 'X':
            move = human_player.get_move(game)
        else:
            move = ai_player.get_move(game)
        
        # Make the move
        game.make_move(move)
    
    # Print the final state of the game
    print(game)
    
    # Print the result of the game
    print("Game Over!")
    print("Result:", game.get_result())

if __name__ == "__main__":
    main()
