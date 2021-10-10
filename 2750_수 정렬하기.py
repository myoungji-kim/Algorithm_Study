from sys import stdin

N = []

for i in range(int(stdin.readline())):
    N.append(int(stdin.readline()))

N.sort()

for i in range(len(N)):
    print(N[i])