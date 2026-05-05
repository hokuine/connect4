from board import Board

    
# 0 is empty | 1 is player | 2 is bot
EMPTY = 0
PLAYER_PIECE = 1
BOT_PIECE = 2


def evaluate_window(window: list, piece):
    score = 0
    # switch scoring
    opponent_piece = PLAYER_PIECE if piece == BOT_PIECE else BOT_PIECE

    piece_count = window.count(piece)
    empty_count = window.count(EMPTY)
    opponent_count = window.count(opponent_piece)

    # winning move gives mst points
    if piece_count == 4:
        score += 100
    # connect 3 is second big priority
    elif piece_count == 3 and empty_count == 1:
        score += 5

    elif piece_count == 2 and empty_count == 2:
        score += 2

    # prioritize on blocking enemies winning move
    if opponent_count == 3 and empty_count == 1:
        score -= 4

    return score


def score_position(board, piece):
    score = 0

    # Prefer the center column because it creates the most possible connect fours.
    center_column = [board.grid[row][3] for row in range(6)]
    score += center_column.count(piece) * 3

    # Score horizontal windows.
    for row in range(6):
        row_array = board.grid[row]
        for col in range(4):
            window = row_array[col:col + 4]
            score += evaluate_window(window, piece)

    # Score vertical windows.
    for col in range(7):
        col_array = [board.grid[row][col] for row in range(6)]
        for row in range(3):
            window = col_array[row:row + 4]
            score += evaluate_window(window, piece)

    # Score positive diagonal windows.
    for row in range(3):
        for col in range(4):
            window = [board.grid[row + i][col + i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Score negative diagonal windows.
    for row in range(3):
        for col in range(4):
            window = [board.grid[row + 3 - i][col + i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score
