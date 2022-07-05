from sys import stdin

N = int(stdin.readline())
blank = N - 1

for i in range(1, N + 1):
    print("*" * i, " " * blank * 2, "*" * i, sep="")
    blank -= 1

blank += 2

for i in range(N - 1, 0, -1):
    print("*" * i, " " * blank * 2, "*" * i, sep="")
    blank += 1
