from sys import stdin
N = int(stdin.readline())
row = N
star = "*"
blank = " "

for i in range(2*row-1):
    if (i<row):
        print(blank * N, star * ((2*i)+1), sep="")
        N -= 1
    elif (i>=row):
        N += 1
        print(blank * (N+1), star * (2*i-N*2), sep="")