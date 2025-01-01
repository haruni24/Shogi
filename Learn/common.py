import cshogi
import numpy as np

def board_to_input(board):
    input = list()
    np_board = np.array(board.pieces)
    for i in range(1,cshogi.WPROM_ROOK+1):
        if i==15 or i==16:
            continue
        input.append((i==np_board).reshape(9, 9))
    return np.array(input)

def random_play(board):
    while True:
        if board.is_game_over() or len(board.history)>100:
            break
        move = np.random.choice(list(board.legal_moves))
        board.push(move)
    return 1-board.turn