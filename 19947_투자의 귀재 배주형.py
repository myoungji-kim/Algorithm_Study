from sys import stdin

H, Y = map(int, stdin.readline().split())
dp = [0] * (Y + 1)
dp[0] = H

for i in range(1, Y + 1):
    if i >= 5:
        dp[i] = max(int(dp[i - 5] * 1.35), int(dp[i - 3] * 1.2), int(dp[i - 1] * 1.05))
    elif i >= 3:
        dp[i] = max(int(dp[i - 3] * 1.2), int(dp[i - 1] * 1.05))
    else:
        dp[i] = int(dp[i - 1] * 1.05)

print(dp[-1])