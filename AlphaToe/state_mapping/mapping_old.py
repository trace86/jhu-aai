from typing import List, Tuple
#import snoop
from pprint import pprint
import os
import pandas as pd

attacks = pd.read_csv("io/commands.csv")

def show_intention(attack_id):
    print("Using vulnerability/exploit: {0} (linked port {1})...".format(attacks.iloc[attack_id]["exploit_name"],
                                                                         attacks.iloc[attack_id]["linked_port"]))

def write_file(fname, command):
    with open(f"io/{fname}.txt", "w") as f:  # not appending on purpose
        f.write(command)

def read_file(fname):
    with open(f"io/{fname}.txt") as f:
        return f.read()

def get_latest_move(prev_state, current_state):
    return [(i, j) for i in range(0, len(prev_state)) for j in range(0, len(current_state[0])) if prev_state[i][j] != current_state[i][j]][0]


def adjacency_check(i, j, matrix, num_neighbors=2):
    min_i = 0
    min_j = 0
    max_i = len(matrix) - 1
    max_j = len(matrix[0]) - 1

    start_pos_i = i + (i - min_i) if i - num_neighbors < min_i else i - num_neighbors
    start_pos_j = j + (j - min_j) if j - num_neighbors < min_j else j - num_neighbors
    end_pos_i = i + (max_i - i) if i + num_neighbors > max_i else i + num_neighbors
    end_pos_j = j + (max_j - j) if j + num_neighbors > max_j else j + num_neighbors

    locs = []
    for _i in range(start_pos_i, end_pos_i + 1):
        for _j in range(start_pos_j, end_pos_j + 1):
            locs.append((_i, _j))
    horizontal = [loc for loc in locs if loc[0] == i]
    vertical = [loc for loc in locs if loc[1] == j]
    diagonal = [loc for loc in locs if loc[0] == loc[1]]
    antidiagonal = [loc for loc in locs if loc[0] + loc[1] == (i + j)]
    return {
        "horizontal": horizontal,
        "vertical": vertical,
        "diagonal": diagonal,
        "antidiagonal": antidiagonal
    }


def horizontal_left_search(i, j, matrix, num_neighbors, symbol):
    min_i = 0
    min_j = 0
    max_i = len(matrix) - 1
    max_j = len(matrix[0]) - 1

    xs = []
    for n in range(1, num_neighbors + 1):
        _i = i
        _j = j - n
        if _i >= min_i and _j >= min_j and _i <= max_i and _j <= max_j:
            xs.append(matrix[_i][_j])
    if len(xs) != num_neighbors:
        return False
    return all(item == symbol for item in xs)


def horizontal_right_search(i, j, matrix, num_neighbors, symbol):
    min_i = 0
    min_j = 0
    max_i = len(matrix) - 1
    max_j = len(matrix[0]) - 1

    xs = []
    for n in range(1, num_neighbors + 1):
        _i = i
        _j = j + n
        if _i >= min_i and _j >= min_j and _i <= max_i and _j <= max_j:
            xs.append(matrix[_i][_j])
    if len(xs) != num_neighbors:
        return False
    return all(item == symbol for item in xs)


def vertical_up_search(i, j, matrix, num_neighbors, symbol):
    min_i = 0
    min_j = 0
    max_i = len(matrix) - 1
    max_j = len(matrix[0]) - 1

    xs = []
    for n in range(1, num_neighbors + 1):
        _i = i - n
        _j = j
        if _i >= min_i and _j >= min_j and _i <= max_i and _j <= max_j:
            xs.append(matrix[_i][_j])
    if len(xs) != num_neighbors:
        return False
    return all(item == symbol for item in xs)


def vertical_down_search(i, j, matrix, num_neighbors, symbol):
    min_i = 0
    min_j = 0
    max_i = len(matrix) - 1
    max_j = len(matrix[0]) - 1

    xs = []
    for n in range(1, num_neighbors + 1):
        _i = i + n
        _j = j
        if _i >= min_i and _j >= min_j and _i <= max_i and _j <= max_j:
            xs.append(matrix[_i][_j])
    if len(xs) != num_neighbors:
        return False
    return all(item == symbol for item in xs)


def diagonal_left_search(i, j, matrix, num_neighbors, symbol):
    min_i = 0
    min_j = 0
    max_i = len(matrix) - 1
    max_j = len(matrix[0]) - 1

    xs = []
    for n in range(1, num_neighbors + 1):
        _i = i - n
        _j = j - n
        if _i >= min_i and _j >= min_j and _i <= max_i and _j <= max_j:
            xs.append(matrix[_i][_j])
    if len(xs) != num_neighbors:
        return False
    return all(item == symbol for item in xs)


def diagonal_right_search(i, j, matrix, num_neighbors, symbol):
    min_i = 0
    min_j = 0
    max_i = len(matrix) - 1
    max_j = len(matrix[0]) - 1

    xs = []
    for n in range(1, num_neighbors + 1):
        _i = i + n
        _j = j + n
        if _i >= min_i and _j >= min_j and _i <= max_i and _j <= max_j:
            xs.append(matrix[_i][_j])
    if len(xs) != num_neighbors:
        return False
    return all(item == symbol for item in xs)


def antidiagonal_left_search(i, j, matrix, num_neighbors, symbol):
    min_i = 0
    min_j = 0
    max_i = len(matrix) - 1
    max_j = len(matrix[0]) - 1

    xs = []
    for n in range(1, num_neighbors):
        _i = i - n
        _j = j - n
        if _i >= min_i and _j >= min_j and _i <= max_i and _j <= max_j:
            xs.append(matrix[_i][_j])
    if len(xs) != num_neighbors + 1:
        return False
    return all(item == symbol for item in xs)


def antidiagonal_right_search(i, j, matrix, num_neighbors, symbol):
    min_i = 0
    min_j = 0
    max_i = len(matrix) - 1
    max_j = len(matrix[0]) - 1

    xs = []
    for n in range(0, num_neighbors + 1):
        _i = i + n
        _j = j + n
        if _i >= min_i and _j >= min_j and _i <= max_i and _j <= max_j:
            xs.append(matrix[_i][_j])
    if len(xs) != num_neighbors + 1:
        return False
    return all(item == symbol for item in xs)

def check_move_made_inbetween_two_moves(i, j, matrix, symbol):
    horizontal = all([horizontal_left_search(i, j, matrix, num_neighbors=1, symbol=symbol),
                      horizontal_right_search(i, j, matrix, num_neighbors=1, symbol=symbol)])
    vertical = all([vertical_up_search(i, j, matrix, num_neighbors=1, symbol=symbol),
                    vertical_down_search(i, j, matrix, num_neighbors=1, symbol=symbol)])
    diagonal = all([diagonal_right_search(i, j, matrix, num_neighbors=1, symbol=symbol),
                    diagonal_left_search(i, j, matrix, num_neighbors=1, symbol=symbol)])
    antidiagonal = all([antidiagonal_right_search(i, j, matrix, num_neighbors=1, symbol=symbol),
                        antidiagonal_left_search(i, j, matrix, num_neighbors=1, symbol=symbol)])
    return any([horizontal, vertical, diagonal, antidiagonal])

def check_move_made_inbetween_three_moves(i, j, matrix, symbol):
    # scenario x X x x
    horizontal1 = all([horizontal_left_search(i, j, matrix, num_neighbors=1, symbol=symbol),
                     horizontal_right_search(i, j, matrix, num_neighbors=2, symbol=symbol)])
    vertical1 = all([vertical_up_search(i, j, matrix, num_neighbors=1, symbol=symbol),
                    vertical_down_search(i, j, matrix, num_neighbors=2, symbol=symbol)])
    diagonal1 = all([diagonal_right_search(i, j, matrix, num_neighbors=1, symbol=symbol),
                   diagonal_left_search(i, j, matrix, num_neighbors=2, symbol=symbol)])
    antidiagonal1 = all([antidiagonal_right_search(i, j, matrix, num_neighbors=1, symbol=symbol),
                    antidiagonal_left_search(i, j, matrix, num_neighbors=2, symbol=symbol)])
    # scenario x x X x
    horizontal2 = all([horizontal_left_search(i, j, matrix, num_neighbors=2, symbol=symbol),
                     horizontal_right_search(i, j, matrix, num_neighbors=1, symbol=symbol)])
    vertical2 = all([vertical_up_search(i, j, matrix, num_neighbors=2, symbol=symbol),
                    vertical_down_search(i, j, matrix, num_neighbors=1, symbol=symbol)])
    diagonal2 = all([diagonal_right_search(i, j, matrix, num_neighbors=2, symbol=symbol),
                   diagonal_left_search(i, j, matrix, num_neighbors=1, symbol=symbol)])
    antidiagonal2 = all([antidiagonal_right_search(i, j, matrix, num_neighbors=2, symbol=symbol),
                    antidiagonal_left_search(i, j, matrix, num_neighbors=1, symbol=symbol)])
    return any([horizontal1, vertical1, diagonal1, antidiagonal1, horizontal2, vertical2, diagonal2, antidiagonal2])

def eval_attacker_move(i, j, matrix, num_neighbors, symbol):
    return any([
        horizontal_left_search(i, j, matrix, num_neighbors, symbol),
        horizontal_right_search(i, j, matrix, num_neighbors, symbol),
        vertical_up_search(i, j, matrix, num_neighbors, symbol),
        vertical_down_search(i, j, matrix, num_neighbors, symbol),
        diagonal_right_search(i, j, matrix, num_neighbors, symbol),
        diagonal_left_search(i, j, matrix, num_neighbors, symbol),
        antidiagonal_right_search(i, j, matrix, num_neighbors, symbol),
        antidiagonal_left_search(i, j, matrix, num_neighbors, symbol)])

def is_first_move(i, j, matrix, symbol):
    count = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == symbol:
                count += 1
            if count >= 2:
                return False
    return True

def parse(strng, ip_address="192.168.56.101"):
    strng = strng.replace(" || ", "\n")
    strng = strng.replace("[address]", ip_address)
    return strng

def eval_attacker_3x3(i, j, matrix, attack_id=0):

    exploit_file = "exploit_3x3"
    symbol=1
    if is_first_move(i, j, matrix, symbol=symbol):
        # save scanned ports to a list
        #return "port scan"
        return parse(attacks.iloc[attack_id]["scan_command"])
    if not eval_attacker_move(i, j, matrix, num_neighbors=1, symbol=symbol):
        return "NOP"
    if eval_attacker_move(i, j, matrix, num_neighbors=2, symbol=symbol):
        try:
            if read_file(exploit_file) == "exploit initiated":
                #return "run exploit -- game over, attacker wins!"
                return attacks.iloc[attack_id]["exploit_command"]
        except FileNotFoundError:
            #return "use exploit, run exploit -- game over, attacker wins!"
            return "{0}\n{1}".format(attacks.iloc[attack_id]["use_command"], attacks.iloc[attack_id]["exploit_command"])
    if check_move_made_inbetween_two_moves(i, j, matrix, symbol):
        try:
            if read_file(exploit_file) == "exploit initiated":
                #return "run exploit -- game over, attacker wins!"
                return attacks.iloc[attack_id]["exploit_command"]
        except FileNotFoundError:
            #return "use exploit, run exploit -- game over, attacker wins!"
            return "{0}\n{1}".format(attacks.iloc[attack_id]["use_command"], attacks.iloc[attack_id]["exploit_command"])
    if eval_attacker_move(i, j, matrix, num_neighbors=1, symbol=symbol):
        write_file(exploit_file, "exploit initiated")
        # retrieve command based on port from a list of ports and command from db of commands
        #return "use and set commands to commence"
        return "{0}\n{1}".format(attacks.iloc[attack_id]["use_command"], parse(attacks.iloc[attack_id]["set_command"]))
    return "NOP"

def eval_attacker_5x5(i, j, matrix):
    exploit_file = "exploit_5x5"
    set_file = "set_5x5"
    symbol=1
    if is_first_move(i, j, matrix, symbol=symbol):
        # save scanned ports to a list
        return "port scan"
    if not eval_attacker_move(i, j, matrix, num_neighbors=1, symbol=symbol):
        return "NOP"
    if eval_attacker_move(i, j, matrix, num_neighbors=3, symbol=symbol):
        try:
            if read_file(set_file) == "set initiated":
                return "run exploit -- game over, attacker wins!"
        except FileNotFoundError:
            return "set exploit, run exploit -- game over, attacker wins!"
    if check_move_made_inbetween_three_moves(i, j, matrix, symbol):
        try:
            if read_file(set_file) == "set initiated":
                return "run exploit -- game over, attacker wins!"
        except FileNotFoundError:
            return "set exploit, run exploit -- game over, attacker wins!"
    if eval_attacker_move(i, j, matrix, num_neighbors=2, symbol=symbol):
        try:
            if read_file(exploit_file) == "exploit initiated":
                return "set exploit"
        except FileNotFoundError:
            write_file(set_file, "set initiated")
            return "init exploit, set exploit"
    if check_move_made_inbetween_two_moves(i, j, matrix, symbol):
        try:
            if read_file(exploit_file) == "exploit initiated":
                return "set exploit"
        except FileNotFoundError:
            write_file(set_file, "set initiated")
            return "init exploit, set exploit"
    if eval_attacker_move(i, j, matrix, num_neighbors=1, symbol=symbol):
        write_file(exploit_file, "exploit initiated")
        return "use command to commence exploit"
    return "NOP"

def eval_move(prev_state, current_state, attack_id):
    move = get_latest_move(prev_state, current_state)
    i = move[0]
    j = move[1]
    if current_state[i][j] == 1: # attacker
        if len(current_state) == 3:
            return eval_attacker_3x3(i, j, current_state, attack_id)
        if len(current_state) == 5:
            return eval_attacker_5x5(i, j, current_state, attack_id)
    elif current_state[i][j] == 2: # defender
        return "defender moves go here..."
    else:
        return "something has gone terribly wrong" # ruh roh