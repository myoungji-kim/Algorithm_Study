from sys import stdin

A, B, V = map(int, stdin.readline().split())

V -= B
cnt = V // (A - B)

if V % (A - B) == 0:
    print(cnt)
else:
    print(cnt + 1)
