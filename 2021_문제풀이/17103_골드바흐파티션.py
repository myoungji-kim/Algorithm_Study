from sys import stdin

array = [False, False] + ([True] * (1000000 - 1))

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

for i in range(int(stdin.readline())):
    cnt = 0
    n = int(stdin.readline())

    if n == 0: break

    for j in range(n//2+1):
        if array[j] and array[n-j]:
            cnt += 1
    print(cnt)