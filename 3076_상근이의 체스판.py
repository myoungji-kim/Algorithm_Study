from sys import stdin

R, C = map(int, stdin.readline().split())
A, B = map(int, stdin.readline().split())
black = True

for _ in range(R):
    save = black
    for i in range(A):
        for j in range(C):
            if black:
                print('X' * B, end="")
                black = False
            else:
                print('.' * B, end="")
                black = True
        black = save
        print("")
    if black:
        black = False
    else:
        black = True

