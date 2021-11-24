from sys import stdin

for i in range(int(stdin.readline())):
    count = 0
    score = list(map(int, stdin.readline().split()))
    aver = sum(score[1:]) // score[0]
    for j in range(1, len(score)):
        if score[j] > aver:
            count += 1
    result = round(count / (len(score) - 1) * 100, 3)
    result = "{:.3f}".format(result)

    print(result, "%", sep="")
