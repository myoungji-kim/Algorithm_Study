from sys import stdin

N, K = map(int, stdin.readline().split())
cnt = 0

# for else 문
for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1

    if cnt == K:
        print(i)
        break
else:
    print(-1)
