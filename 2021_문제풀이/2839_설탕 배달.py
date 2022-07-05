from sys import stdin

N = int(stdin.readline())
cnt = 0

while True:
    N = N - 5 if N % 5 == 0 else N - 3
    cnt += 1

    if N <= 0:
        print(cnt) if N == 0 else print(-1)
        exit()
