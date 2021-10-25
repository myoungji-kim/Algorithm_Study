from sys import stdin

while True:
    words = stdin.readline().rstrip()
    result = 0

    if words == '#':
        exit()

    for i in words:
        if i in 'aAeEiIoOuU':
            result += 1

    print(result)
