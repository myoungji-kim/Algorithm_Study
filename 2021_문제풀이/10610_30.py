from sys import stdin

N = list(stdin.readline().rstrip())
N.sort(reverse=True)

if N[len(N)-1] != '0' or sum(map(int, N)) % 3 != 0:
    print(-1)
else:
    print(''.join(N))