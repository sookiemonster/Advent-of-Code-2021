FILENAME = "input.txt"

def shift_list(arr, new_val):
    result = []
    for i in range(len(arr)):
        if i != 0:
            result.append(arr[i])
    result.append(new_val)
    return result


def main():
    with open(FILENAME) as file_input:
        result = 0
        prev_rows = []
        prev_sum = 0
        for line in file_input:
            if len(prev_rows) < 3:
                prev_rows.append(int(line))
            else:
                prev_rows = shift_list(prev_rows, int(line))

                if sum(prev_rows) > prev_sum:
                    result += 1
                prev_sum = sum(prev_rows)

        print(result)

main()