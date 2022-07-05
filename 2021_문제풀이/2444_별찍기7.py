from sys import stdin

N = int(stdin.readline())
blank = N - 1

for i in range(1, N + 1):
    print(" " * blank, "*" * ((2 * i) - 1), sep="")
    blank -= 1

blank = 0

for i in range(N - 1, 0, -1):
    blank += 1
    print(" " * blank, "*" * ((2 * i) - 1), sep="")
