from Services.TicTacToeGame import TicTacToeGame

def it_should_draw_an_empty_board():
    size: int = 3
    symbols: list = ['O', 'X']
    empty_symbol: str = '_'

    game: TicTacToeGame = TicTacToeGame(size, symbols, empty_symbol)
    assert game.draw_board() == "\n_ _ _ \n_ _ _ \n_ _ _"

if __name__ == "__main__":
    it_should_draw_an_empty_board()
    print("Everything passed")