from sys import stdin

N = int(stdin.readline())
A = set(list(map(int, stdin.readline().split())))
M = int(stdin.readline())
B = list(map(int, stdin.readline().split()))

for i in range(M):
    if B[i] in A:
        print(1)
    else:
        print(0)
