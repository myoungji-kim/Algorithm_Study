from sys import stdin

while True:
    input = list(map(int, stdin.readline().split()))
    if input == [0, 0, 0]:
        exit()

    for i in range(3):
        input[i] *= input[i]

    input.sort()
    print("right") if input[0]+input[1] == input[2] else print("wrong")