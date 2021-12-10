FILENAME = "input.txt"

def fuel_cost(steps):
    return int(steps * (1 + steps) / 2)

def differences(pos_list, final_pos):
    # print("Final Position: %s" % (final_pos))
    result = [fuel_cost(abs(pos - final_pos)) for pos in pos_list]
    # print(["Initial Pos: %s, Fuel Cost: %s" % (pos, abs(pos - final_pos)) for pos in pos_list])
    return result

def main():
    data = []
    with open(FILENAME, 'r') as file_input:
        data = list(map(int, file_input.read().split(",")))

    # data.sort()
    length = max(data) - min(data)
    fuel_list = []
    for i in range(length + 1):
        fuel_list.append(sum(differences(data, i)))
    
    # for i in range(len(fuel_list)):
        # print("Position %s : Fuel Cost %s" % (i, fuel_list[i]))
    print(min(fuel_list))
        
if __name__ == '__main__':
    main()