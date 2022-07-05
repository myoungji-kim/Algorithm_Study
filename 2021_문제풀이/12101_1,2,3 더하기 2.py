from sys import stdin

n, k = map(int, stdin.readline().split())
dp = [["1"], ["1+1", "2"], ["1+1+1", "1+2", "2+1", "3"]]

for i in range(n - 3):
    temp = []
    for a in dp[-1]:
        temp.append(a + "+1")
    for b in dp[-2]:
        temp.append(b + "+2")
    for c in dp[-3]:
        temp.append(c + "+3")
    dp.append(temp)
    dp[-1].sort()

if len(dp[n - 1]) >= k:
    print(dp[n - 1][k - 1])
else:
    print(-1)
