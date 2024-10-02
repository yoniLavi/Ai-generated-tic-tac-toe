import unittest
from player import AIPlayer
from game import Game

class TestAIPlayer(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_ai_makes_moves(self):
        ai1 = AIPlayer()
        ai2 = AIPlayer()
        ai1.set_strength_level(3)
        ai2.set_strength_level(3)

        game = Game()
        moves_made = 0
        while not game.is_game_over() and moves_made < 9:
            move = ai1.get_move(game) if game.get_current_player() == 'X' else ai2.get_move(game)
            game.make_move(move)
            moves_made += 1

        self.assertGreater(moves_made, 0, "No moves were made in the game")
        self.assertNotEqual(game.get_board(), [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], "Board remained unchanged")

    def test_ai_levels(self):
        wins = {1: 0, 2: 0, 3: 0}
        draws = 0
        games_per_matchup = 100  # Reduced for quicker testing

        for level1 in [1, 2, 3]:
            for level2 in range(level1 + 1, 4):
                print(f"\nTesting AI Level {level1} vs AI Level {level2}")
                for game_num in range(games_per_matchup):
                    ai1 = AIPlayer()
                    ai1.set_strength_level(level1)
                    ai2 = AIPlayer()
                    ai2.set_strength_level(level2)
                    
                    result = self.play_game(ai1, ai2)
                    if result == 'draw':
                        draws += 1
                    else:
                        wins[int(result)] += 1
                    
                    if game_num % 10 == 0:
                        print(f"Game {game_num + 1}: {'Draw' if result == 'draw' else f'AI Level {result} wins'}")

        print(f"\nFinal Results:")
        print(f"AI Level Wins: {wins}")
        print(f"Draws: {draws}")

        total_games = sum(wins.values()) + draws
        self.assertEqual(total_games, games_per_matchup * 3, f"Expected {games_per_matchup * 3} games, but played {total_games}")
        self.assertGreater(sum(wins.values()), 0, "No games were won by any AI")

    def test_optimal_moves(self):
        ai = AIPlayer()
        ai.set_strength_level(3)  # Set to hardest difficulty

        # Test blocking opponent's win (horizontal)
        game = Game()
        game.board = [
            ['X', 'X', ' '],
            [' ', 'O', ' '],
            [' ', ' ', ' ']
        ]
        game.current_player = 'O'
        move = ai.get_move(game)
        self.assertEqual(move, (0, 2), "AI should block opponent's horizontal win")

        # Test blocking opponent's win (vertical)
        game = Game()
        game.board = [
            ['X', ' ', ' '],
            ['X', 'O', ' '],
            [' ', ' ', ' ']
        ]
        game.current_player = 'O'
        move = ai.get_move(game)
        self.assertEqual(move, (2, 0), "AI should block opponent's vertical win")

        # Test blocking opponent's win (diagonal)
        game = Game()
        game.board = [
            ['X', ' ', ' '],
            [' ', 'X', ' '],
            [' ', 'O', ' ']
        ]
        game.current_player = 'O'
        move = ai.get_move(game)
        self.assertEqual(move, (2, 2), "AI should block opponent's diagonal win")

        # Test taking winning move
        game = Game()
        game.board = [
            ['O', 'O', ' '],
            [' ', 'X', ' '],
            ['X', ' ', ' ']
        ]
        game.current_player = 'O'
        move = ai.get_move(game)
        self.assertEqual(move, (0, 2), "AI should take the winning move")

        # Test preferring center
        game = Game()
        game.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        game.current_player = 'X'
        move = ai.get_move(game)
        self.assertEqual(move, (1, 1), "AI should prefer the center")

    def play_game(self, player1, player2):
        game = Game()
        current_player = player1
        while not game.is_game_over():
            move = current_player.get_move(game)
            game.make_move(move)
            current_player = player2 if current_player == player1 else player1

        result = game.get_result()
        if result == 'X wins':
            return str(player1.strength_level)
        elif result == 'O wins':
            return str(player2.strength_level)
        else:
            return 'draw'

if __name__ == '__main__':
    unittest.main()
