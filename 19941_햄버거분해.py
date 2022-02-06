from sys import stdin

N, K = map(int, stdin.readline().split())
lst = list(stdin.readline().rstrip())
dp = [0] * len(lst)
for i in range(len(lst)):
    if lst[i] == "P":
        if i + K >= len(lst):
            x = len(lst)
        else:
            x = i + K + 1

        if i - K < 0:
            y = 0
        else:
            y = i - K

        for j in range(y, x):
            if dp[j] == 0 and lst[j] == "H":
                dp[j] = 1
                break
print(dp.count(1))
