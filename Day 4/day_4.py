import copy
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
        self.board = arr_2D.copy()
        self.original = copy.deepcopy(arr_2D)

    def __str__(self):
        result = ""
        for row in self.board:
            str_row = [str(num) for num in row]
            for element_counter in range(len(str_row)):
                if len(str_row[element_counter]) < 2:
                    str_row[element_counter] = " " + str_row[element_counter]
            result += ' '.join(str_row)
            result += "\n"
        return result

    def get_original(self):
        result = ""
        for row in self.original:
            str_row = [str(num) for num in row]
            for element_counter in range(len(str_row)):
                if len(str_row[element_counter]) < 2:
                    str_row[element_counter] = " " + str_row[element_counter]
            result += ' '.join(str_row)
            result += "\n"
        return result

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

    # Returns if the updated board results in a bingo
    def update_board(self, number):
        for row_counter in range(len(self.board)):
            for col_counter in range(len(self.board)):
                if self.board[row_counter][col_counter] == number:
                    self.board[row_counter][col_counter] = -1
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
    

    winning_boards = []
    for number in directions:
        board_index = 0
        while board_index < len(boards):
            bingo_object = boards[board_index]
            if bingo_object.update_board(number):
                winning_boards.append([bingo_object, number])
                boards.pop(board_index)
                board_index -= 1
            board_index += 1

    print(winning_boards[-1][0].sum_unmarked())
    print(winning_boards[-1][0].sum_unmarked() * winning_boards[-1][1])

main()