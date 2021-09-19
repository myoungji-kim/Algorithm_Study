import math, sys
from itertools import combinations

N = int(sys.stdin.readline())
for i in range(N):
    sum = 0
    L = list(map(int, sys.stdin.readline().split()))[1:]
    A = list(combinations(L, 2))
    for j in range(len(A)):
        sum += math.gcd(A[j][0], A[j][1])
    print(sum)