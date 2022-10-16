import sys
sys.path.append('../Models')
from Models import Player

class Player:
    def __init__(self, symbol: str):
        if len(symbol) > 1:
            raise Exception("symbol cannot be more than one character")
        self.symbol = symbol
    
    def enter_move(self, board: list[str]):
        print("this should implement a move deciding mechanism")