FILENAME = "input.txt"

def str_2D_arr(string):
    result = []
    rows = string.split("\n")
    for line in rows:
        row_temp = list(map(int, line.split()))
        if len(row_temp) > 0:
            result.append(row_temp)
    return result

class Bingo_Board:
    def __init__(self, arr_2D):
        self.ROW_LENGTH = 5
        self.COLUMN_LENGTH = 5
        self.board = arr_2D

    def sum_unmarked(self):
        result = 0
        for row in self.board:
            for cell in row:
                if cell != -1:
                    result += cell
        return result

    def check_bingo(self, row, col):
        # Check for horizontal bingo
        marked_num = 0
        for cell in self.board[row]: 
            if cell == -1:
                marked_num += 1
        if marked_num >= self.ROW_LENGTH:
            return True
        
        # Check for vertical bingo
        marked_num = 0
        for row in self.board:
            if row[col] == -1:
                marked_num += 1
        
        if marked_num >= self.ROW_LENGTH:
            return True
        return False

    def update_board(self, number):
        for row_counter in range(len(self.board)):
            for col_counter in range(len(self.board)):
                if self.board[row_counter][col_counter] == number:
                    self.board[row_counter][col_counter] =  -1
                    if self.check_bingo(row_counter, col_counter):
                        return True
        return False

def main():
    data = []
    boards = []
    with open(FILENAME, "r") as file_input:
        data = file_input.read().split("\n\n")

    directions = list(map(int, data.pop(0).split(",")))
    for arr_2D in data:
        boards.append(Bingo_Board(str_2D_arr(arr_2D)))
    
    for number in directions:
        for bingo_object in boards:
            if bingo_object.update_board(number):
                print(bingo_object.sum_unmarked() * number)
                return 0
    return 0

main()