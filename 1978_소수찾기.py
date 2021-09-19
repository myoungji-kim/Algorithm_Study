from sys import stdin

N = int(stdin.readline())
L = list(map(int, stdin.readline().split()))
cnt = 0

def check(x):
    if (x == 1):
        return False
    for i in range(2, x):
        if (x % i) == 0:
            return False
    return True

for i in range(N):
    if (check(L[i])==True):
        cnt += 1

print(cnt)