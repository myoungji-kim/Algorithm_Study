import math
from sys import stdin

N, M = map(int, stdin.readline().split())

print(math.factorial(N) // (math.factorial(M) * math.factorial(N-M)))