from sys import stdin

for i in range(int(stdin.readline())):
    math = list(stdin.readline().rstrip().split())
    result = 0

    for j in math:
        if j == '@':
            result *= 3

        elif j == '%':
            result += 5

        elif j == '#':
            result -= 7

        else:
            result = float(j)

    print("{:.2f}".format(result))
