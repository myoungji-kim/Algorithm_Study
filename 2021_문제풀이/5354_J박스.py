from sys import stdin

for i in range(int(stdin.readline())):
    A = int(stdin.readline())
    for j in range(A):
        if j == 0 or j == A - 1:
            print("#" * A)
        else:
            B = "J" * (A - 2)
            print("#", end="")
            print(B, end="")
            print("#")

    print("")