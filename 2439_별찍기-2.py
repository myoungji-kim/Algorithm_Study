import sys
n = int(sys.stdin.readline())
m = n-1
star = "*"

for i in range(n) :
    bin = " " * m
    print (bin+star)
    m -= 1
    star += "*"
