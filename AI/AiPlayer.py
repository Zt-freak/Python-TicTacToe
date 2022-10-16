import random
from Models.Player import Player

class AiPlayer(Player):
    def __init__(self, symbol: str):
        super().__init__(symbol)

    def enter_move(self, board: list[str], empty_symbol: str):
        full_indexes: list[int] = list(range(0, len(board)))
        available: list[int] = list(filter(lambda value: board[value] == empty_symbol, full_indexes))
        return random.choice(available)