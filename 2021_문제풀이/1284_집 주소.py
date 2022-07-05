from sys import stdin

width = {'0': 4, '1': 2, '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 3, '8': 3, '9': 3}

while True:
    nums = stdin.readline().rstrip()
    result = 1

    if nums == '0':
        exit()

    for i in nums:
        result += width[i] + 1

    print(result)
