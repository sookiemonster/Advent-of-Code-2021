FILENAME = "input.txt"

def str_2D_arr(string):
    result = []
    line_no = 0
    for line in string:
        result.append([])
        for c in line:
            if c.isnumeric():
                result[line_no].append(int(c))
        line_no += 1
    return result

def freq(arr):
    result = [0, 0] # FREQ of 0 & 1 respectively
    for num in arr:
        result[num] += 1
    return result

def get_column_list(arr_2D):
    result = []

    for col_num in range(len(arr_2D[0])):
        result.append([])
        for row_num in range(len(arr_2D)):
            result[col_num].append(int(arr_2D[row_num][col_num]))
    return result

def main():
    freq_list = []
    gamma = ""
    epsilon = ""
    with open(FILENAME) as file_input: 
        cols = get_column_list(str_2D_arr(file_input))
        for col in cols:
            freq_list.append(freq(col))
    for freq_item in freq_list:
        if freq_item[0] > freq_item[1]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    print(int(gamma, 2) * int(epsilon, 2))

main()