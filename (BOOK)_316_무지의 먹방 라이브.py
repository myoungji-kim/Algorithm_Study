from sys import stdin

food_times = list(map(int, stdin.readline().split()))
k = int(stdin.readline())
time = 0

while True:
    for i in range(len(food_times)):
        if time == k:
            print(i+1)
            exit()
        if food_times[i] > 0:
            food_times[i] -= 1
            time += 1