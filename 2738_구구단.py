import sys
n = int(sys.stdin.readline())
m = 1

for i in range(9):
    print(n, "*", m, "=", n*m)
    m += 1