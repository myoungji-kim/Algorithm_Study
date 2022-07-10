from sys import stdin

N = int(stdin.readline())
nums = [list(map(int, stdin.readline().split())) for _ in range(N)]
diag1, diag2 = 0, 0
maxNum = -1
for i in range(N):
    if sum(nums[i]) > maxNum:
        maxNum = sum(nums[i])
    tmp = 0

    for j in range(N):
        tmp += nums[j][i]
    if tmp > maxNum:
        maxNum = tmp

    diag1 += nums[i][i]
    diag2 += nums[N - i - 1][i]

if diag1 > maxNum:
    maxNum = diag1
if diag2 > maxNum:
    maxNum = diag2

print(maxNum)

