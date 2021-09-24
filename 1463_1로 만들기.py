from sys import stdin

X = int(stdin.readline())
cnt = 0

while True:
    if X % 3 == 0:
        X //= 3

    elif X % 2 == 0:
        X //= 2

    else:
        X -= 1

    cnt += 1
    print('X: ',X)

    if X == 1:
        print(cnt)
        exit()