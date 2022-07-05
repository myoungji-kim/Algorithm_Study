from sys import stdin

A, I = map(int, stdin.readline().split())
answer = (I - 1) * A + 1
print(answer)
