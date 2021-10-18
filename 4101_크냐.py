from sys import stdin

while True:
    X, Y = map(int, stdin.readline().split())

    if X == 0 and Y == 0:
        exit()

    if X > Y:
        print("Yes")
    elif X <= Y:
        print("No")