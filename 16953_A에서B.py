from sys import stdin

A, B = map(int, stdin.readline().split())
cnt = 1

while B > A:
    B = (B - 1) // 10 if B % 10 == 1 else B / 2
    cnt += 1

print(cnt) if B == A else print(-1)
