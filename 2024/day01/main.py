def readInput(filename = "input.txt") -> str:
    input = open(filename, "r").read()

    return input

def construct_arrays(input: str):
    first_list = []
    second_list = []

    building_num = ""

    for ch in input:
        if ch != " " and ch != "\n":
            building_num += ch
        else:
            if len(building_num) <= 0:
                continue
            else:
                target_list = first_list if ch == " " else second_list
                target_list.append(int(building_num))
                building_num = ""

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
