from sys import stdin

N, M = map(int, stdin.readline().split())
nums = sorted(list(map(int, stdin.readline().split())))
lt, rt = 0, len(nums) - 1

while True:
    p1 = (lt + rt) // 2
    if nums[p1] == M:
        print(p1 + 1)
        break
    elif nums[p1] < M:
        lt = p1
    else:
        rt = p1
