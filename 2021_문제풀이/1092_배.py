from sys import stdin

N = int(stdin.readline())
crane = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
box = list(map(int, stdin.readline().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

if crane[0] < box[0]:
    print(-1)
else:
    time = 0
    while len(box) > 0:
        time += 1
        for i in crane:
            for j in range(len(box)):
                if i >= box[j]:
                    del box[j]
                    break
    print(time)
