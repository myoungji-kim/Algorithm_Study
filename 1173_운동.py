from sys import stdin

N, m, M, T, R = map(int, stdin.readline().split())
workTime = 0
restTime = 0
hearts = m

if m + T > M:
    print(-1)
    exit()

while workTime != N:
    if hearts + T <= M:
        hearts += T
        workTime += 1
    else:
        hearts = m if hearts - R < m else hearts - R
        restTime += 1

print(workTime + restTime)
