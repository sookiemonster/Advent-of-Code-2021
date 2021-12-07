import re
FILENAME = "input.txt"
# INDICES
X1 = 0
Y1 = 1
X2 = 2
Y2 = 3

def freq_dict(arr_2D):
    result = {}
    for row in arr_2D:
        tuple_row = (row[0], row[1])
        if tuple_row in result:
            result[tuple_row] += 1
        else:
            result[tuple_row] = 1
    return result

def get_points(x1, y1, x2, y2):
    result = []
    if x1 == x2:
        if (y2 > y1):
            for y in range(y1, y2 + 1):
                result.append([x1, y])
        else:
            for y in range(y2, y1 + 1):
                result.append([x1, y])
    elif y1 == y2:
        if (x2 > x1):
            for x in range(x1, x2 + 1):
                result.append([x, y1])
        else: 
            for x in range(x2, x1 + 1):
                result.append([x, y1])
    else:
        counter = 0
        # Left to right
        if (x1 < x2):
            for x in range(x1, x2 + 1):
                if (y1 < y2):
                    # going up
                    result.append([x, y1 + counter])
                else:
                    # going down
                    result.append([x, y1 - counter])
                counter += 1
        # Right to left
        else:
            for x in range(x1, x2 - 1, -1):
                if (y1 < y2):
                    # going up
                    result.append([x, y1 + counter])
                else:
                    # going down
                    result.append([x, y1 - counter])
                counter += 1
    return result

def main():
    data = []
    with open(FILENAME, "r") as file_input:
        rows = [re.split(",| -> ", line) for line in file_input.read().split("\n")]
        row_counter = 0
        for row in rows:
            data.append([])
            for element in row:
                if element.isnumeric():
                    data[row_counter].append(int(element))

            row_counter += 1
    
    points = []
    for row in data:
        for point in get_points(row[X1], row[Y1], row[X2], row[Y2]):
            if len(point) > 0:
                points.append(point)

    overlaps = list(freq_dict(points).values())
    overlaps = list(filter(lambda n : n > 1, overlaps))
    print(len(overlaps))

if __name__ == "__main__":
    main()