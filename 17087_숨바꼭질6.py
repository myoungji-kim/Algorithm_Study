import math
from sys import stdin

bin = []
X, S = stdin.readline().split()
brother = list(map(int, stdin.readline().split()))

for i in range(len(brother)):
    bin.append(abs(int(S)-brother[i]))

for i in range(len(bin)):
    bin[0] = math.gcd(bin[0], bin[i])

print(bin[0])