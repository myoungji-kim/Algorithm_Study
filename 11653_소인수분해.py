from sys import stdin

N = int(stdin.readline())
d = 2

while (N != 1):
    if (N % d == 0):
        N = N / d
        print(d)
    else:
        d += 1