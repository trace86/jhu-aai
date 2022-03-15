import game_eval
board5_3 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]
board5_4 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]

move = game_eval.get_state_mapping_evaluation(board5_3, board5_4, debug=True)
print(move)