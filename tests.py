from engine.board import Board

b = Board()

# test drop and print
b.drop_piece(3, 1)
b.drop_piece(3, 1)
b.drop_piece(3, 1)
b.drop_piece(3, 1)
print(b)
print("vertical win:", b.check_win(1))   # True

# test horizontal
b2 = Board()
b2.drop_piece(0, 1)
b2.drop_piece(1, 1)
b2.drop_piece(2, 1)
b2.drop_piece(3, 1)
print(b2)
print("horizontal win:", b2.check_win(1))  # True

# test valid columns
b3 = Board()
print("valid cols:", b3.valid_columns())   # [0,1,2,3,4,5,6]

# test is_full returns False on empty board
print("is full:", b3.is_full())            # False