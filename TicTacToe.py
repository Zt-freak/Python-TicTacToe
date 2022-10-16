from Services.TicTacToeGame import TicTacToeGame

# Game Configuration
size: int = 3
symbols: list = ['O', 'X']
empty_symbol: str = '_'

game: TicTacToeGame = TicTacToeGame(size, symbols, empty_symbol)
game.start()