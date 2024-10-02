import unittest
from game import Game
from player import AIPlayer

class TestGameBasics(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_board(self):
        self.assertEqual(self.game.get_board(), [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])

    def test_make_move(self):
        self.game.make_move((0, 0))
        self.assertEqual(self.game.get_board()[0][0], "X")
        self.assertEqual(self.game.get_current_player(), "O")

    def test_win_condition(self):
        moves = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)]
        for move in moves:
            self.game.make_move(move)
        self.assertTrue(self.game.is_game_over())
        self.assertEqual(self.game.get_result(), "X wins")

    def test_tie_condition(self):
        moves = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0), (1, 2), (2, 1), (2, 0), (2, 2)]
        for move in moves:
            self.game.make_move(move)
        self.assertTrue(self.game.is_game_over())
        self.assertEqual(self.game.get_result(), "Tie")

    def test_ai_player_makes_valid_move(self):
        ai_player = AIPlayer()
        for level in [1, 2, 3]:
            ai_player.set_strength_level(level)
            game = Game()
            move = ai_player.get_move(game)
            self.assertIsInstance(move, tuple)
            self.assertEqual(len(move), 2)
            self.assertTrue(0 <= move[0] < 3 and 0 <= move[1] < 3)
            self.assertEqual(game.get_board()[move[0]][move[1]], " ")

if __name__ == '__main__':
    unittest.main()
