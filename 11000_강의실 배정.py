import heapq
from sys import stdin

N = int(stdin.readline())
time = [list(map(int, stdin.readline().split())) for i in range(N)]
time.sort()

Q = []
heapq.heappush(Q, time[0][1])
for i in range(1, N):
    if time[i][0] < Q[0]:
        heapq.heappush(Q, time[i][1])
    else:
        heapq.heappop(Q)
        heapq.heappush(Q, time[i][1])
print(len(Q))
