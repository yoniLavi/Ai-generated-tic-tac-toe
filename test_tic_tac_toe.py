import unittest
from unittest.mock import patch
from game import Game
from player import HumanPlayer, AIPlayer


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.human_player = HumanPlayer()
        self.ai_player = AIPlayer()

    def test_initial_game_state(self):
        self.assertFalse(self.game.is_game_over())
        self.assertEqual(self.game.get_current_player(), "X")
        self.assertEqual(self.game.get_result(), None)

    def test_make_move(self):
        self.game.make_move((0, 0))
        self.assertEqual(self.game.get_board()[0][0], "X")
        self.assertEqual(self.game.get_current_player(), "O")

    def test_invalid_move(self):
        self.game.make_move((0, 0))
        with self.assertRaises(ValueError):
            self.game.make_move((0, 0))

    def test_game_over_horizontal(self):
        self.game.make_move((0, 0))
        self.game.make_move((1, 0))
        self.game.make_move((0, 1))
        self.game.make_move((1, 1))
        self.game.make_move((0, 2))
        self.assertTrue(self.game.is_game_over())
        self.assertEqual(self.game.get_result(), "X wins")

    def test_game_over_vertical(self):
        self.game.make_move((0, 0))
        self.game.make_move((0, 1))
        self.game.make_move((1, 0))
        self.game.make_move((0, 2))
        self.game.make_move((2, 0))
        self.assertTrue(self.game.is_game_over())
        self.assertEqual(self.game.get_result(), "X wins")

    def test_game_over_diagonal(self):
        self.game.make_move((0, 0))
        self.game.make_move((0, 1))
        self.game.make_move((1, 1))
        self.game.make_move((0, 2))
        self.game.make_move((2, 2))
        self.assertTrue(self.game.is_game_over())
        self.assertEqual(self.game.get_result(), "X wins")

    def test_game_over_draw(self):
        moves = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0), (1, 2), (2, 1), (2, 0), (2, 2)]
        for move in moves:
            self.game.make_move(move)
        self.assertTrue(self.game.is_game_over())
        self.assertEqual(self.game.get_result(), "Tie")

    @patch("builtins.input", side_effect=["1"])
    def test_human_player_input(self, mock_input):
        move = self.human_player.get_move(self.game)
        self.assertEqual(move, (0, 0))

    def test_ai_player_move(self):
        move = self.ai_player.get_move(self.game)
        self.assertIsInstance(move, tuple)
        self.assertEqual(len(move), 2)
        self.assertTrue(0 <= move[0] <= 2 and 0 <= move[1] <= 2)


if __name__ == "__main__":
    unittest.main()
