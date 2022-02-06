from collections import Counter
from sys import stdin

n = int(stdin.readline())
nList = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
mList = list(map(int, stdin.readline().split()))
count = Counter(nList)

for i in range(m):
    if mList[i] in count:
        print(count[mList[i]], end=' ')
    else:
        print(0, end=' ')