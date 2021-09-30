from collections import deque
from sys import stdin

N = int(stdin.readline())
nums = deque([i for i in range(1, N+1)])

if N == 1:
    print(N)
    exit()

while True:
    nums.popleft()
    nums.append(nums[0])
    nums.popleft()

    if len(nums) == 1:
        print(nums.pop())
        exit()
