from sys import stdin

cnt = 1

while True:
    L, P, V = map(int, stdin.readline().split())

    if L == 0 and P == 0 and V == 0:
        exit()
    else:
        if V % P > L:
            result = ((V // P) * L) + L
        else:
            result = ((V // P) * L) + (V % P)
        print("Case ", cnt, ": ", result, sep="")
        cnt += 1
