FILENAME = "input.txt"
DAYS = 256

def update(fish_list):
    result = [0] * 9
    for days_left in range(9):
        if days_left == 0:
            result[8] = fish_list[days_left]
            result[6] = fish_list[days_left]
        else:
            result[days_left - 1] += fish_list[days_left]
    return result

def freq_readable(freq_list):
    result = []
    index = 0
    for frequency in freq_list:
        for n in range(frequency):
            result.append(index)
        index += 1
    return result

def main():
    data = []
    with open(FILENAME, "r") as file_input:
        data = list(map(int, file_input.read().split(',')))
    
    fish_list = [0] * 9
    for fish in data:
        fish_list[fish] += 1
    
    for day in range(DAYS):
        fish_list = update(fish_list)
        # print("After %s day(s) : %s" % (day + 1, freq_readable(fish_list)))
    
    print(sum(fish_list))


if __name__ == '__main__':
    main()