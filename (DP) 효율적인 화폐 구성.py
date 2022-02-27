from sys import stdin

n, m = map(int, stdin.readline().split())

lst = []
for i in range(n):
    lst.append(int(stdin.readline()))
dp = [10001] * (m + 1)
dp[0] = 0

for i in range(n):
    for j in range(lst[i], m + 1):
        if dp[j - lst[i]] != 10001:
            dp[j] = min(dp[j], dp[j - lst[i]] + 1)

print(-1) if dp[m] == 10001 else print(dp[m])

