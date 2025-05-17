from unittest import TestCase

from common.base_game_spec import BaseGameSpec
from techniques.monte_carlo import monte_carlo_tree_search_uct


class _LambdaBugGameSpec(BaseGameSpec):
    def __init__(self):
        pass

    def new_board(self):
        return 0

    def apply_move(self, board_state, move, side):
        return move[1]

    def available_moves(self, board_state):
        if board_state == 0:
            return [(0, 1), (1, -1)]
        return []

    def has_winner(self, board_state):
        return board_state

    def board_dimensions(self):
        return (1,)


class TestMonteCarloTreeSearchUCT(TestCase):
    def test_lambda_takes_single_argument(self):
        game_spec = _LambdaBugGameSpec()
        result, move = monte_carlo_tree_search_uct(game_spec, game_spec.new_board(), 1, 10)
        self.assertIn(move, [(0, 1), (1, -1)])
        self.assertIsInstance(result, float)
