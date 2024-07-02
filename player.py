import math
import random

class Participant():
    def __init__(self, symbol):
        self.symbol = symbol

    def next_move(self, board_game):
        pass

class Human(Participant):
    def __init__(self, symbol):
        super().__init__(symbol)

    def next_move(self, board_game):
        valid_move = False
        move = None
        while not valid_move:
            square = input(self.symbol + "'s turn. Input move (0-9): ")
            try:
                move = int(square)
                if move not in board_game.get_available_moves():
                    raise ValueError
                valid_move = True
            except ValueError:
                print('Invalid move. Try again.')
        return move

class AI(Participant):
    def __init__(self, symbol):
        super().__init__(symbol)

    def next_move(self, board_game):
        if len(board_game.get_available_moves()) == 9:
            square = random.choice(board_game.get_available_moves())
        else:
            square = self.minimax(board_game, self.symbol)['position']
        return square

    def minimax(self, state, player):
        max_player = self.symbol
        min_player = 'O' if player == 'X' else 'X'

        if state.current_winner == min_player:
            return {'position': None, 'score': 1 * (state.num_empty_spaces() + 1) if min_player == max_player else -1 * (
                        state.num_empty_spaces() + 1)}
        elif not state.has_empty_spaces():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for move in state.get_available_moves():
            state.place_move(move, player)
            sim_score = self.minimax(state, min_player)
            state.board[move] = ' '
            state.current_winner = None
            sim_score['position'] = move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
