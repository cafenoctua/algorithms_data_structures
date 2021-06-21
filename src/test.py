import sys


def filter_sum(line: list) -> int:
    return sum([i for i in line if i <= 10000])


sums = 0
for line in sys.stdin:
    sums += filter_sum(list(map(int, line.split())))
print(sums, end="")
