from Models.Player import Player

class AiPlayer(Player):
    def __init__(self, symbol: str):
        super().__init__(symbol)

    def enter_move(self, board: list[str]):
        print("this should implement a move deciding mechanism")