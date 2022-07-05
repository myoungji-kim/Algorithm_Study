from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
dp = [0] * n

if n == 1:
    print(0)
    exit()

for i in range(nums[0] + 1):
    dp[i] = 1

for i in range(1, len(dp)):
    if dp[i] == 0:
        print(-1)
        exit()

    for j in range(nums[i]):
        j += 1
        if i + j >= len(dp):
            print(dp[-1])
            exit()

        elif dp[i + j] == 0:
            dp[i + j] = dp[i] + 1
