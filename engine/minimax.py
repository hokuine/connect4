from board import Board

    
# 0 is empty | 1 is player | 2 is bot
EMPTY = 0
PLAYER_PIECE = 1
BOT_PIECE = 2


def evaluate_window(window: list, piece):
    score = 0
    opponent_piece = PLAYER_PIECE if piece == BOT_PIECE else BOT_PIECE

    piece_count = window.count(piece)
    empty_count = window.count(EMPTY)
    opponent_count = window.count(opponent_piece)


    if piece_count == 4:
        score += 100
    elif piece_count == 3 and empty_count == 1:
        score += 5
    elif piece_count == 2 and empty_count == 2:
        score += 2
    if opponent_count == 3 and empty_count == 1:
        score -= 4

    return score


def score_position(board, piece):
    score = 0


    center_column = [board.grid[row][3] for row in range(6)]
    score += center_column.count(piece) * 3

    for row in range(6):
        row_array = board.grid[row]
        for col in range(4):
            window = row_array[col:col + 4]
            score += evaluate_window(window, piece)

    for col in range(7):
        col_array = [board.grid[row][col] for row in range(6)]
        for row in range(3):
            window = col_array[row:row + 4]
            score += evaluate_window(window, piece)
    for row in range(3):
        for col in range(4):
            window = [board.grid[row + i][col + i] for i in range(4)]
            score += evaluate_window(window, piece)

    for row in range(3):
        for col in range(3, 7):
            window = [board.grid[row + i][col - i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

def winning_move(board, piece):
    return board.check_win(piece)

def minimax(board, depth, alpha, beta, maximisingplayer):
    valid_locations = Board.valid_columns()
    is_terminal = board.check_win(1) or board.check_win(2) or board.is_full()
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, 2):
                return (None, 9999999)
            if winning_move(board, 1):
                return (None, -9999999)
            else:
                return (None, 0)
        else:
            return (None, score_position(board, 2))
