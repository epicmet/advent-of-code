def readInput(filename = "input.txt") -> str:
    file = open(filename).read()

    return file

def is_safe_report(report: str) -> bool:
    report_arr = report.split(" ")
    is_asc = int(report_arr[1]) - int(report_arr[0]) > 0

    for i in range(len(report_arr) - 1): # iter `i` until the one to the last element
        num = int(report_arr[i])
        next_num = int(report_arr[i + 1])
        diff = next_num - num

        if (is_asc and diff < 0) or \
           (not is_asc and diff > 0) or \
            (abs(diff) > 3 or abs(diff) < 1):
            return False

    return True

def part_one():
    safe_reports = 0
    for line in readInput().splitlines():
        if is_safe_report(line):
            safe_reports += 1

    print(f"Part one: {safe_reports}")


if __name__ == "__main__":
    part_one()
