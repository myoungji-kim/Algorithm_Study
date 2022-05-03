from sys import stdin
from collections import deque

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    nums = deque(list(map(int, stdin.readline().split())))
    count = 0

    while True:
        top = max(nums)
        # 1. 뽑기
        if nums[0] == top:
            count += 1
            nums.popleft()
            if m == 0:
                break
            else:
                m -= 1

        # 2. 뒤로 보내기
        else:
            nums.append(nums.popleft())
            if m == 0:
                m = len(nums) - 1
            else:
                m -= 1

    print(count)
