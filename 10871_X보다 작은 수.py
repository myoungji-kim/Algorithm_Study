import sys
N, X = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
R = []

for i in range(N):
    if (L[i] < X):
        R.append(L[i])

print(" ".join(map(str, R)))