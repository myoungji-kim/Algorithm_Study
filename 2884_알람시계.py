import sys

H, M = map(int, sys.stdin.readline().split())

if (M-45 < 0):
    M = 60+(M-45)
    if (H-1>=0):
        H -= 1
    else:
        H = 23
else:
    M -= 45

print(H, M)