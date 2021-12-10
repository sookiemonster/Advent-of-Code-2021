FILENAME = 'test_short.txt'
patterns = {2 : 1, 4 : 4, 3 : 7, 7 : 8} # Number of Signals : Corresponding Number

# Find 1: Get combo 2,5 ~
# Find 7: Get definite 0 ~
# Find 4: Get combo 1, 3 
# Find 9: Get definite 6
# Find 8: Get definite 4 or deduce definite 4
# Find 5: Get definite 5, deduce definite 2
# Find 2: Get definite 3, deduce defintie 1 

# Connections List Format
#   0000
#  1    2
#  1    2
#   3333
#  4    5
#  4    5
#   6666

def difference(str1, str2):
    result = ''
    if len(str1) < len(str2):
        for c in str2:
            if c not in str1:
                result += c
    else:
        for c in str1:
            if c not in str2:
                result += c
    return result

def split_string(string):
    return [c for c in string]

def isNine(known0, comb25, comb13, signal):
    if len(signal) == 6:
        known = known0 + comb13 + comb25
        for c in known:
            if c not in signal:
                return False
        return True
    return False
     
def deduce(signal_list):
    all_connected = False
    connections = [''] * 7
    reference = [''] * 10

    while(not all_connected):
        for signal in signal_list:
            if len(signal) in patterns:
                if not reference[patterns[len(signal)]]:
                    reference[patterns[len(signal)]] = signal
                if (not(connections[0]) and reference[1] and reference[7]):
                    connections[0] = difference(reference[1], reference[7])
                if len(reference[4]) > 2 and reference[1] and reference[4]:
                    reference[patterns[4]] = difference(reference[1], reference[4])
            if (not(connections[6]) and connections[0] and reference[1] and reference[4] and isNine(connections[0], reference[1], reference[4], signal)):
                print("KNOWNS %s" % (connections[0] + reference[1] + reference[4]))
                connections[6] = difference(connections[0] + reference[1] + reference[4], signal)
                all_connected = True
    print("REF %s" % reference)
    print("CON %s" % connections)

def main():
    data = []
    
    with open(FILENAME, 'r') as file_input:
        rows =  file_input.read().split('\n')
        for row in rows: 
            temp_row = row.split(' | ')
            data.append([temp_row[0].split(), temp_row[1].split()])

    for row in data: 
        deduce(row[0])
    
if __name__ == '__main__':
    main()