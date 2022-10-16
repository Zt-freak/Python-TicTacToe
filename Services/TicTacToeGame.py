class TicTacToeGame:
    def __init__(self, size: int, symbols: list, empty_symbol: str):
        self.size: int = size
        self.symbols: list = symbols
        self.empty_symbol: str = empty_symbol
        self.current_symbol: str = symbols[0]
        self.game_over: bool = False
        self.turn: int = 1
        self.board: list = [empty_symbol] * (size * size)

    def draw_board(self):
        board_string: str = ""
        for index, tile in enumerate(self.board):
            if index % self.size == 0:
                board_string += '\n'
            board_string += tile + " "
        return board_string

    def input_symbol(self, index: int):
        if index < 0 or index > len(self.board) or self.board[index] != self.empty_symbol:
            print("invalid index value")
            return
        self.board[index] = self.current_symbol

    def check_win(self):
        full_indexes: list = list(range(0, len(self.board)))
        current_symbol_indexes: list = []

        for index, tile in enumerate(self.board):
            if tile == self.current_symbol:
                current_symbol_indexes.append(index)
        
        for index in range(0, self.size):
            col_indexes: list = list(filter(lambda value: value % self.size == index, full_indexes))
            row_indexes: list = list(filter(lambda value: value >= index * self.size and value < index * self.size + self.size, full_indexes))
            if all(x in current_symbol_indexes for x in col_indexes) or all(x in current_symbol_indexes for x in row_indexes):
                self.game_over = True
            
        diag1_indexes: list = [x*(self.size+1) for x in range(0, self.size)]
        diag2_indexes: list = [x*(self.size-1) + (self.size-1) for x in range(0, self.size)]
        if all(x in current_symbol_indexes for x in diag1_indexes) or all(x in current_symbol_indexes for x in diag2_indexes):
            self.game_over = True

        if self.game_over:
            print("congratulations! player " + self.current_symbol + " won the game!")
            print(self.draw_board())
            return
        elif not self.empty_symbol in self.board:
            print("It is a tie!")
            print(self.draw_board())
            self.game_over = True

    def start(self):
        print("This is the start of Tic Tac Toe")

        while self.game_over == False:
            self.current_symbol = self.symbols[self.turn % len(self.symbols)]
            print("It's turn: "+ str(self.turn) + " and player " + self.current_symbol + " is at play")

            print(self.draw_board())
            print("enter the index at which you want to place your symbol (indexing starts at 0)")
            self.input_symbol(int(input()))

            self.check_win()

            self.turn += 1