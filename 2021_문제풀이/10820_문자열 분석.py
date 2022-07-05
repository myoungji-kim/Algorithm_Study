# Q1. for line in sys.stdin 으로 하면 한줄 공백 생김
# Q2. rstrip('/n')과 rstrip()의 차이는?

import sys

# 임의의 여러줄 입력 받기
while True:
    inputWords = list(sys.stdin.readline().rstrip('/n'))
    # 1: Lower / 2: Upper / 3: Num / 4: Blank
    cnt = [0] * 4

    # 종료
    if not inputWords:
        break

    # 구현
    for i in range(len(inputWords)) :
        if   (inputWords[i].islower()) : cnt[0] += 1
        elif (inputWords[i].isupper()) : cnt[1] += 1
        elif (inputWords[i].isdigit()) : cnt[2] += 1
        elif (inputWords[i] == ' ')    : cnt[3] += 1

    # 결과 출력
    print(" ".join(map(str, cnt)))
