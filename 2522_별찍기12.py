from sys import stdin

N = int(stdin.readline())
blank = N - 1

for i in range(N):
    print(" " * blank, "*" * (N - blank), sep="")
    blank -= 1

blank = 0

for i in range(N - 1):
    blank += 1
    print(" " * blank, "*" * (N - blank), sep="")
