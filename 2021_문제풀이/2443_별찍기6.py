from sys import stdin

N = int(stdin.readline())
blank = 0
for i in range(N, 0, -1):
    print(" " * blank, "*" * ((i * 2) - 1), sep="")
    blank += 1
