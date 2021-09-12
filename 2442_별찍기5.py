from sys import stdin
N = int(stdin.readline())
star = "*"
blank = " "

for i in range(N):
    print(blank*(N-1), star*((i*2)+1), sep="")
    N -= 1