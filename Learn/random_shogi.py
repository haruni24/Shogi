import matplotlib.pyplot as plt
import cshogi

board = cshogi.Board()

def display_board(board):
    fig, ax = plt.subplots(figsize=(6, 6))
    # ボードのグリッドを描画
    for x in range(10):
        ax.plot([x, x], [0, 9], color='black')
        ax.plot([0, 9], [x, x], color='black')
    
    # 駒の位置を描画
    for square in range(81):
        piece = board.piece(square)
        if piece is not None:
            x, y = divmod(square, 9)
            ax.text(y + 0.5, 8.5 - x, cshogi.PIECE_SYMBOLS.get(piece, "?"), ha='center', va='center', fontsize=12)
    
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    ax.axis('off')
    plt.show()

display_board(board)