from board import Board

def minimax(board, depth, alpha, beta, maximising):
    valid_positions = Board.valid_columns(board)