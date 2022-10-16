from Services.TicTacToeGame import TicTacToeGame
from Models.Player import Player
from Models.HumanPlayer import HumanPlayer
from AI.AiPlayer import AiPlayer

def it_should_draw_an_empty_board():
    size: int = 3
    players: list[Player] = [
        AiPlayer('O'),
        HumanPlayer('X')
    ]
    empty_symbol: str = '_'

    game: TicTacToeGame = TicTacToeGame(size, players, empty_symbol)
    assert game.draw_board() == "\n_ _ _ \n_ _ _ \n_ _ _"

if __name__ == "__main__":
    it_should_draw_an_empty_board()
    print("Everything passed")