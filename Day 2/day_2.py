FILENAME = "input.txt"

def get_move(direction, dist):
    if ("forward" in direction):
        return [dist, 0]
    elif ("up" in direction):
        return [0, -1 * dist]
    elif ("down" in direction):
        return [0, dist]

def main():
    result = [0, 0]
    with open(FILENAME) as file_input:
        for line in file_input:
            temp = line.split()
            move = get_move(temp[0], int(temp[1]))
            result[0] += move[0]
            result[1] += move[1]
    print(result[0] * result[1])

main()