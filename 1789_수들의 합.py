from sys import stdin

S = int(stdin.readline())
result = 0
i = 0

while True:
    result += i

    if result == S:
        print(i)
        exit()
    elif result > S:
        print(i-1)
        exit()

    i += 1