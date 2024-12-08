from typing import List

def readInput(filename = "input.txt") -> str:
    file = open(filename).read()

    return file

def is_safe_report(report: List[int]) -> bool:
    is_asc = report[1] - report[0] > 0

    for i in range(len(report) - 1): # iter `i` until the one to the last element
        num = report[i]
        next_num = report[i + 1]
        diff = next_num - num

        if (is_asc and diff < 0) or \
           (not is_asc and diff > 0) or \
            (abs(diff) > 3 or abs(diff) < 1):
            return False

    return True

def part_one():
    safe_reports = 0
    for line in readInput().splitlines():
        report = [int(x) for x in line.split(" ")]
        if is_safe_report(report):
            safe_reports += 1

    print(f"Part one: {safe_reports}")

def part_two():
    safe_reports = 0
    for line in readInput().splitlines():
        report = [int(x) for x in line.split(" ")]

        # I really tried to don't brute force, it took more time that it should
        # Then I found out there is probably no perfect solution, people also use
        # brute force.
        # I can make it better and try to remove only the indexes that I know might cause
        # problem, but what ever.
        anyOk = False
        for i in range(len(report)):
            if is_safe_report(report[:i] + report[i+1:]):
                anyOk = True
        if anyOk: safe_reports += 1

    print(f"Part two: {safe_reports}")


if __name__ == "__main__":
    part_one()
    part_two()
