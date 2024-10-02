import unittest
from game import Game

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def assertBoardEqual(self, board1, board2):
        self.assertEqual(board1, board2, f"Boards are not equal:\n{board1}\n!=\n{board2}")

    def make_moves(self, moves):
        for move in moves:
            self.game.make_move(move)

    def assert_game_state(self, expected_board, expected_player, expected_result):
        self.assertBoardEqual(self.game.get_board(), expected_board)
        self.assertEqual(self.game.get_current_player(), expected_player)
        self.assertEqual(self.game.get_result(), expected_result)
