from board import Board
from minimax import winning_move, score_position, evaluate_window

# test evaluate_window
print("=== evaluate_window ===")
print(evaluate_window([1, 1, 1, 1], 1))   # 100 - win
print(evaluate_window([1, 1, 1, 0], 1))   # 5 - threatening
print(evaluate_window([1, 1, 0, 0], 1))   # 2 - building
print(evaluate_window([2, 2, 2, 0], 1))   # -4 - opponent threatening
print(evaluate_window([0, 0, 0, 0], 1))   # 0 - empty

# test winning_move
print("\n=== winning_move ===")
b = Board()
b.drop_piece(0, 1)
b.drop_piece(1, 1)
b.drop_piece(2, 1)
b.drop_piece(3, 1)
print(b)
print("player wins:", winning_move(b, 1))   # True
print("bot wins:", winning_move(b, 2))      # False

# test score_position
print("\n=== score_position ===")
b2 = Board()
b2.drop_piece(3, 2)  # bot in centre
b2.drop_piece(3, 2)
b2.drop_piece(3, 2)
print(b2)
print("bot score:", score_position(b2, 2))    # should be positive
print("player score:", score_position(b2, 1)) # should be lower