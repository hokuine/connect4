# 0 is empty | 1 is player | 2 is bot
#


class board:
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
        ""

    # this is hard
    def check_win(self, player):
        # im going to first check if theres horizontal 4s
        for row in self.grid:
            for i in range(4):
                group = row[i:i+4]
                if all(cell == player for cell in group):
                    return True
            # vertical
            
        for row in self.grid:
            for i in range(6):
                index=row[i]


    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.grid)

    