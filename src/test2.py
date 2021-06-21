# import sys
# for line in sys.stdin:
#    print(line, end="")
from collections import defaultdict

N = int(input())
D = int(input())
places = [input().split(".") for _ in range(N)]
places_dict = defaultdict()
for place in places:
    address = ".".join(place[-1 * D :])
    if address in places_dict.keys():
        places_dict[address] += 1
    else:
        places_dict[address] = 1

for place, cnt in zip(places_dict.keys(), places_dict.values()):
    print(f"{place} {cnt}")
