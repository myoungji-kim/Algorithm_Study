from sys import stdin
N = int(stdin.readline())
star = "*"
blank = " "

for i in range(N):
    print(blank*i, star*N, sep="")
    N -= 1