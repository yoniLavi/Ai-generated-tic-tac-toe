import unittest
from player import AIPlayer
from game import Game

class TestAIPlayer(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_ai_levels(self):
        wins = {1: 0, 2: 0, 3: 0}
        draws = 0
        games_per_matchup = 100

        for _ in range(games_per_matchup):
            for level1 in [1, 2, 3]:
                for level2 in range(level1 + 1, 4):
                    ai1 = AIPlayer()
                    ai1.set_strength_level(level1)
                    ai2 = AIPlayer()
                    ai2.set_strength_level(level2)
                    
                    result = self.play_game(ai1, ai2)
                    if result == 'draw':
                        draws += 1
                    else:
                        wins[int(result)] += 1

        print(f"AI Level Wins: {wins}")
        print(f"Draws: {draws}")

        # Assert that higher levels win more often
        self.assertGreater(wins[3], wins[2])
        self.assertGreater(wins[3], wins[1])
        self.assertGreater(wins[2], wins[1])

    def test_optimal_moves(self):
        ai = AIPlayer()
        ai.set_strength_level(3)  # Set to hardest difficulty

        # Test blocking opponent's win
        self.game.board = [
            ['X', 'X', ' '],
            [' ', 'O', ' '],
            [' ', ' ', ' ']
        ]
        move = ai.get_move(self.game)
        self.assertEqual(move, (0, 2), "AI should block opponent's win")

        # Test taking winning move
        self.game.board = [
            ['O', 'O', ' '],
            [' ', 'X', ' '],
            ['X', ' ', ' ']
        ]
        move = ai.get_move(self.game)
        self.assertEqual(move, (0, 2), "AI should take the winning move")

        # Test creating a fork
        self.game.board = [
            ['O', ' ', ' '],
            [' ', 'X', ' '],
            [' ', ' ', ' ']
        ]
        move = ai.get_move(self.game)
        self.assertIn(move, [(0, 2), (2, 0), (2, 2)], "AI should create a fork")

    def play_game(self, player1, player2):
        self.game.reset()
        current_player = player1
        while not self.game.is_game_over():
            move = current_player.get_move(self.game)
            self.game.make_move(move)
            current_player = player2 if current_player == player1 else player1

        result = self.game.get_result()
        if result == 'X':
            return '1'
        elif result == 'O':
            return '2'
        else:
            return 'draw'

if __name__ == '__main__':
    unittest.main()
