import math
import time
from player import Human, AI

class TicTacToeGame():
    def __init__(self):
        self.board = self.create_board()
        self.current_winner = None

    @staticmethod
    def create_board():
        board = []
        for space in range(9):
            board.append(' ')
        return board

    def display_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def display_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def place_move(self, square, symbol):
        if self.board[square] == ' ':
            self.board[square] = symbol
            if self.is_winner(square, symbol):
                self.current_winner = symbol
            return True
        return False

    def is_winner(self, square, symbol):
        row_index = math.floor(square / 3)
        row = self.board[row_index*3:(row_index+1)*3]
        if all([s == symbol for s in row]):
            return True
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([s == symbol for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == symbol for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == symbol for s in diagonal2]):
                return True
        return False

    def has_empty_spaces(self):
        return ' ' in self.board

    def num_empty_spaces(self):
        return self.board.count(' ')

    def get_available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def start_game(board_game, x_participant, o_participant, show_game=True):

    if show_game:
        board_game.display_board_nums()

    symbol = 'X'
    while board_game.has_empty_spaces():
        if symbol == 'O':
            square = o_participant.next_move(board_game)
        else:
            square = x_participant.next_move(board_game)
        if board_game.place_move(square, symbol):

            if show_game:
                print(symbol + ' makes a move to square {}'.format(square))
                board_game.display_board()
                print('')

            if board_game.current_winner:
                if show_game:
                    print(symbol + ' wins!')
                return symbol
            symbol = 'O' if symbol == 'X' else 'X'

        time.sleep(.8)

    if show_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_participant = AI('X')
    o_participant = Human('O')
    game = TicTacToeGame()
    start_game(game, x_participant, o_participant, show_game=True)
