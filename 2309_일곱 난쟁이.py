from itertools import combinations
from sys import stdin

heights = [int(stdin.readline()) for i in range(9)]
test = list(combinations(heights, 7))
for i in range(len(test)):
    if sum(test[i]) == 100:
        result = sorted(test[i])
        for j in result:
            print(j)
        exit()
