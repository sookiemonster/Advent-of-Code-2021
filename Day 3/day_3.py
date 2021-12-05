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

def keep_rows(arr_2D, keeper_bit, bit_pos):
    row_counter = 0
    while row_counter < len(arr_2D):
        if arr_2D[row_counter][bit_pos] != keeper_bit:
            arr_2D.pop(row_counter)
            row_counter -= 1
        row_counter += 1
    return arr_2D

def main():
    data = []
    with open(FILENAME) as file_input: 
        data = str_2D_arr(file_input)
            
    bit_pos = 0
    oxygen_list = data.copy()
    carbon_list = data.copy()

    for bit_pos in range(len(data[0])):
        oxygen_freq = freq(get_column_list(oxygen_list)[bit_pos])
        most_common_oxygen = oxygen_freq.index(max(oxygen_freq))
        if oxygen_freq[0] == oxygen_freq[1]:
            most_common_oxygen = 1

        carbon_freq = freq(get_column_list(carbon_list)[bit_pos])
        least_common_carbon = carbon_freq.index(min(carbon_freq))
        # Defaults to first element (0 in this case) if frequencies are equal

        # print("_______________________")
        # print("Bit Position: %s" % bit_pos)
        # print("Most Common Oxygen Bit: %s" % most_common_oxygen)
        # print("Least Common Carbon Bit: %s" % least_common_carbon)

        if len(oxygen_list) > 1:
            oxygen_list = keep_rows(oxygen_list, most_common_oxygen, bit_pos)
        if len(carbon_list) > 1:
            carbon_list = keep_rows(carbon_list, least_common_carbon, bit_pos)

        # print("After Removal: ")
        # print(oxygen_list)
        # print(carbon_list)

    oxygen = ""
    carbon = ""
    for bit in oxygen_list[0]:
        oxygen += str(bit)
    for bit in carbon_list[0]:
        carbon += str(bit)
    print(int(oxygen, 2) * int(carbon, 2))

main()