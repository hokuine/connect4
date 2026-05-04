from board import Board

def minimax(board, depth, alpha, beta, maximising):
    valid_positions = Board.valid_columns(board)


def evaluate_window(window: list, piece):
    # this rewards the AI
    # 0 is empty | 1 is player | 2 is bot
    score = 0
    # window is a list
    #winning move
    if window.count(piece) == 4:
        score += 100
    # connect 3
    elif window.count(piece) == 3:
        score += 5
    #connect 2
    elif window.count(piece) == 2:
        score += 2
    

    return score