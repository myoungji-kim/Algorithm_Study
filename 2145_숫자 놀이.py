from sys import stdin

while True:
    input = stdin.readline().rstrip()

    if input == '0':
        exit()

    while len(input) > 1:
        bin = 0
        for i in range(len(input)):
            bin += int(input[i])
        input = str(bin)

    print(input)