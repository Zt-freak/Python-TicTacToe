# Game Configuration
size: int = 3
symbols: list = ['O', 'X']
empty_symbol: str = '_'

# Initialise stating values
current_symbol: str = symbols[0]
game_over: bool = False
turn: int = 1
board: list = [empty_symbol] * (size * size)

# Functions
def draw_board():
    board_string: str = ""
    for index, tile in enumerate(board):
        if index % size == 0:
            board_string += '\n'
        board_string += tile + " "
    return board_string

def input_symbol(index: int):
    if index < 0 or index > len(board) or board[index] != empty_symbol:
        print("invalid index value")
        return
    board[index] = current_symbol

def check_win():
    global game_over

    full_indexes: list = list(range(0, len(board)))
    current_symbol_indexes: list = []

    for index, tile in enumerate(board):
        if tile == current_symbol:
            current_symbol_indexes.append(index)
    
    for index in range(0, size):
        col_indexes: list = list(filter(lambda value: value % size == index, full_indexes))
        row_indexes: list = list(filter(lambda value: value >= index * size and value < index * size + size, full_indexes))
        if all(x in current_symbol_indexes for x in col_indexes) or all(x in current_symbol_indexes for x in row_indexes):
            game_over = True
        
    diag1_indexes: list = [x*(size+1) for x in range(0, size)]
    diag2_indexes: list = [x*(size-1) + (size-1) for x in range(0, size)]
    if all(x in current_symbol_indexes for x in diag1_indexes) or all(x in current_symbol_indexes for x in diag2_indexes):
        game_over = True

    if game_over:
        print("congratulations! player " + current_symbol + "won the game!")
        print(draw_board())
        return
    elif not empty_symbol in board:
        print("It is a tie!")
        print(draw_board())
        game_over = True

# The Game
print("This is the start of Tic Tac Toe")

while game_over == False:
    current_symbol = symbols[turn % len(symbols)]
    print("It's turn: "+ str(turn) + " and player " + current_symbol + " is at play")

    print(draw_board())
    print("enter the index at which you want to place your symbol (indexing starts at 0)")
    input_symbol(int(input()))

    check_win()

    turn += 1