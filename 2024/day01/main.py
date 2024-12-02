def readInput(filename = "input.txt") -> str:
    input = open(filename, "r").read()

    return input

# Parse it better
def construct_arrays(input: str):
    first_list = []
    second_list = []

    building_num = ""

    for ch in input:
        if ch == " ":
            if len(building_num) > 0:
                first_list.append(int(building_num))
                building_num = ""
            else:
                continue
        elif ch == "\n":
            if len(building_num) > 0:
                second_list.append(int(building_num))
                building_num = ""
            else:
                continue
        else:
            building_num += ch

    return first_list, second_list

def main():
    (f, s) = construct_arrays(readInput("test.txt")) # First & Second lists
    f.sort()
    s.sort()

    total_distance = 0
    for i in range(len(f)):
        total_distance += abs(f[i] - s[i])

    print(total_distance)
    return total_distance


if __name__ == "__main__":
    main()
