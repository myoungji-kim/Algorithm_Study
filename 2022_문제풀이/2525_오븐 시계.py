from sys import stdin

A, B = map(int, stdin.readline().split())
C = int(stdin.readline())

hour = A + (B + C) // 60
min = (B + C) % 60

print(hour % 24, min)