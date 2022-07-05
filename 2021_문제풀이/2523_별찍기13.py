from sys import stdin

N = int(stdin.readline())

for i in range(0, N):
    print("*" * (i + 1))

for i in range(N - 1, 0, -1):
    print("*" * i)
