from sys import stdin

N = int(stdin.readline())
first = list(stdin.readline().rstrip())

for i in range(N - 1):
    others = list(stdin.readline().rstrip())
    for j in range(len(first)):
        if first[j] != others[j]:
            first[j] = '?'

print(''.join(first))
