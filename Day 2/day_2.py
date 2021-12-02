FILENAME = "input.txt"
HORIZONTAL = 0
DEPTH = 1
AIM = 2

def get_move(direction, dist, aim):
    if ("forward" in direction):
        return [dist, aim * dist, 0]
    elif ("up" in direction):
        return [0, 0, -1 * dist]
    elif ("down" in direction):
        return [0, 0, dist]

def main():
    result = [0, 0, 0] # Horizontal, Depth, Aim
    with open(FILENAME) as file_input:
        for line in file_input:
            temp = line.split()
            move = get_move(temp[0], int(temp[1]), result[AIM])
            result[HORIZONTAL] += move[HORIZONTAL]
            result[DEPTH] += move[DEPTH]
            result[AIM] += move[AIM]
    print(result[0] * result[1])

main()