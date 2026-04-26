# 0 is empty | 1 is player | 2 is bot
#


class Board:
    def __init__(self):
        self.grid = [[0]*7 for i in range(6)]
    
    def drop_piece(self, col, player):
        for row in reversed(range(6)):
            if self.grid[row][col] == 0:
                self.grid[row][col] = player
                return

    def is_full(self):
        for row in self.grid:
            for i in row:
                if i == 0:
                    return False
        return True

    def valid_columns(self):
        valids = []
        for col in range(7):
            if self.grid[0][col] == 0:
                valids.append(col)
        return valids



    def check_win(self, player):
        # im going to first check if theres horizontal 4s
        for row in self.grid:
            for i in range(4): # because the list has 7 elements and for connect 4 we need 4 next to each other only leading to 4 possible answers
                group = row[i:i+4]
                if all(cell == player for cell in group): #all function returns true if everything is true and false if not
                    return True
            
        # vertical    
        for col in range(7):
            column = [self.grid[row][col] for row in range(6)]
            for i in range(3):
                group = column[i:i+4]
                if all(cell == player for cell in group):
                    return True

        # diagonals
        for row in range(3):
            for col in range(4):
                group = [self.grid[row+i][col+i] for i in range(4)]
                if all(cell == player for cell in group):
                    return True

        for row  in range(3):
            for col in range(3, 7):
                group = [self.grid[row+i][col-i] for i in range(4)]
                if all(cell == player for cell in group):
                    return True

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.grid)

    