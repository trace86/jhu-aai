from copy import deepcopy
from math import inf

import game_play
from game_play import getWinner, getMoves


def ab_minimax(board, depth, player, is_maximizing_player, initial_player, alpha, beta):
    who_won = getWinner(board)
    if depth == 0 or who_won != -1:
        if (who_won == 1 or who_won == 2) and who_won == initial_player:
            score = 10 + depth
        elif who_won == 0:
            score = 0
        else:
            score = -10 - depth
        return [-1, -1, score]

    if is_maximizing_player:
        best_val = [-1, -1, -inf]
        for cell in getMoves(board):
            i, j = cell[0], cell[1]
            board[i][j] = player
            score = ab_minimax(deepcopy(board), deepcopy(depth)-1, 2 if deepcopy(player) == 1 else 1, False,
                               deepcopy(initial_player), deepcopy(alpha), deepcopy(beta))
            board[i][j] = 0
            score[0], score[1] = i, j
            best_val = score if score[2] > best_val[2] else best_val
            alpha = best_val if best_val[2] > alpha[2] else alpha
            if beta[2] <= alpha[2]:
                break
        return best_val

    else:
        best_val = [-1, -1, inf]
        for cell in getMoves(board):
            i, j = cell[0], cell[1]
            board[i][j] = player
            score = ab_minimax(deepcopy(board), deepcopy(depth)-1, 2 if deepcopy(player) == 1 else 1, True,
                               deepcopy(initial_player), deepcopy(alpha), deepcopy(beta))
            board[i][j] = 0
            score[0], score[1] = i, j
            best_val = score if score[2] < best_val[2] else best_val
            beta = best_val if best_val[2] < beta[2] else beta
            if beta[2] <= alpha[2]:
                break
        return best_val


board_5x5 = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
m = ab_minimax(board_5x5, 6, player=1, is_maximizing_player=True, initial_player=1,
               alpha=[-1, -1, -inf], beta=[-1, -1, inf])
print(m)

b = board_5x5
b[m[0]][m[1]] = 1
game_play.printBoard(b)