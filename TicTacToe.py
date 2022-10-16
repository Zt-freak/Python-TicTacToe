from Services.TicTacToeGame import TicTacToeGame
from Models.Player import Player
from Models.HumanPlayer import HumanPlayer
from AI.AiPlayer import AiPlayer

# Game Configuration

size: int = 3
players: list[Player] = [
    AiPlayer('O'),
    HumanPlayer('X')
]
empty_symbol: str = '_'

game: TicTacToeGame = TicTacToeGame(size, players, empty_symbol)
game.start()