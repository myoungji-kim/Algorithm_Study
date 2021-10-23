from itertools import product
from sys import stdin

S1, S2, S3 = map(int, stdin.readline().split())
S1 = [i + 1 for i in range(S1)]
S2 = [i + 1 for i in range(S2)]
S3 = [i + 1 for i in range(S3)]

product = list(product(S1, S2, S3))
sums = [sum(product[i]) for i in range(len(product))]
same = {}

for lst in sums:
    try:
        same[lst] += 1
    except:
        same[lst] = 1

print(max(same, key=same.get))
