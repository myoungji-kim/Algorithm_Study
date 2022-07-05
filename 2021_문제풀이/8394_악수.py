from sys import stdin

n = int(stdin.readline())
hs = [1, 2]

if n == 1:
    print(hs[0])
elif n == 2:
    print(hs[1])
else:
    for i in range(n - 2):
        hs.append(int(str(hs[-1])[-1])+int(str(hs[-2])[-1]))
    print(str(hs[-1])[-1])