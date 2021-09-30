import heapq
from sys import stdin

nums = []
for i in range(int(stdin.readline())):
    X = int(stdin.readline())
    if X == 0:
        print(heapq.heappop(nums)) if len(nums) > 0 else print(0)
    elif X > 0:
        heapq.heappush(nums, X)