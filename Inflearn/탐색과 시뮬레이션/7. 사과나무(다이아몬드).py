from sys import stdin

N = int(stdin.readline())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
lt, rt = N // 2, N // 2
apples = 0

for i in range(N):
    if lt == rt:
        apples += graph[i][lt]
    else:
        apples += sum(graph[i][lt:rt + 1])
        
    if i < N // 2:
        lt -= 1
        rt += 1
    else:
        lt += 1
        rt -= 1

print(apples)
