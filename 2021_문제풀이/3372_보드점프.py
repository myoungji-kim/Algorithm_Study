from sys import stdin

n = int(stdin.readline())
board, dp = [], [[0] * (n + 1)]
for i in range(n):
    board.append(list(map(int, stdin.readline().split())))
    dp.append([0] * (n + 1))

dp[0][0] = 1
a, b = 0, 0

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break
        if dp[i][j] > 0:
            a = board[i][j]
            b = dp[i][j]
            try:
                dp[i + a][j] += b
            except:
                True
            try:
                dp[i][j + a] += b
            except:
                True
        else:
            continue

print(dp[n - 1][n - 1])
