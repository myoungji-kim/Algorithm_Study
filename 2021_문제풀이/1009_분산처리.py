from sys import stdin

for i in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    aa = a % 10

    if aa == 0:
        print(10)

    elif aa in [1, 5, 6]:
        print(aa)

    elif aa in [2, 3, 7, 8]:
        if b % 4 == 0:
            print((aa ** 4) % 10)
        else:
            print((aa ** b) % 10)

    elif aa in [4, 9]:
        if b % 2 == 1:
            print(aa)
        else:
            print((aa ** 2) % 10)
