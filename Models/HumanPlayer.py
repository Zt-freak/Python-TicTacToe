from Models.Player import Player

class HumanPlayer(Player):
    def __init__(self, symbol: str):
        super().__init__(symbol)
        
    def enter_move(self, board: list[str], empty_symbol: str, size: int):
        print("enter the index at which you want to place your symbol (indexing starts at 0)")
        return int(input())