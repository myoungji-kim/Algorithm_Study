import math
from sys import stdin

N = int(stdin.readline())

for i in range(N):
    A, B = map(int, stdin.readline().split())
    print(round(A * B / math.gcd(A, B)))