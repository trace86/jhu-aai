from copy import deepcopy
from math import inf

import game_play
from game_play import getWinner, getMoves


def minimax(board, depth, player, is_maximizing_player, initial_player):
    if is_maximizing_player:
        best_move = [-1, -1, -inf]
    else:
        best_move = [-1, -1, inf]

    who_won = getWinner(board)
    if depth == 0 or who_won != -1:
        if (who_won == 1 or who_won == 2) and who_won == initial_player:
            score = 10 + depth
        elif who_won == 0:
            score = 0
        else:
            score = -10 - depth
        return [-1, -1, score]

    for cell in getMoves(board):
        i, j = cell[0], cell[1]
        board[i][j] = player
        score = minimax(deepcopy(board), deepcopy(depth)-1, 2 if deepcopy(player) == 1 else 1, False, deepcopy(initial_player))
        board[i][j] = 0
        score[0], score[1] = i, j

        if is_maximizing_player:
            if score[2] > best_move[2]:
                best_move = score
        else:
            if score[2] < best_move[2]:
                best_move = score

    return best_move


board_5x5 = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
m = minimax(board_5x5, 3, player=1, is_maximizing_player=True, initial_player=1)
print(m)

b = board_5x5
b[m[0]][m[1]] = 1
game_play.printBoard(b)