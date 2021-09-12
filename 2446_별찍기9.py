from sys import stdin
N = int(stdin.readline())
row = N
star = "*"
blank = " "

for i in range(2*row-1):
    if (i<row):
        print(blank * i, star * ((N*2)-1), sep="")
        N -= 1
    elif (i>=row):
        N += 1
        print(blank * (i-(N*2)), star * ((N*2)+1), sep="")