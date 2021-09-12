import sys
from collections import deque
inputWords = list(sys.stdin.readline().rstrip())

# 괄호 개수
cntOpenBKT  = 0
cntCloseBKT = 0

# Deque, Result
inBKT  = []
outBKT = deque()
result = []

# Case 1 : 공백없이 시작 + 괄호 개수 체크
if (inputWords[0] == ' ' or inputWords.count('<')!=inputWords.count('>')) :
    exit()

for i in range(len(inputWords)) :
    # Case 2 : 괄호 내부 문자열 Stack + 앞,뒤에는 '<,>' 추가
    if (inputWords[i] == '<') :
        result.append("".join(outBKT))
        outBKT = deque()

    if (inputWords[i] == '>') :
        inBKT.append(inputWords[i])
        result.append("".join(inBKT))
        inBKT = []

    if (cntOpenBKT > cntCloseBKT) :
        inBKT.append(inputWords[i])

    # Case 3 : 괄호 외부 문자열 Stack + reverse 효과
    elif (cntOpenBKT == cntCloseBKT) :
        if (inputWords[i] == '>') :
            inBKT.append(inputWords[i])
            result.append("".join(inBKT))
            inBKT = []

        elif (inputWords[i] == ' ') :
            outBKT.append(inputWords[i])
            result.append("".join(outBKT))
            outBKT = deque()

        else :
            outBKT.appendleft(inputWords[i])

# Case 4 : 외부 문자열 남았을 경우 result 에 넣어주기
result.append("".join(outBKT))

print("".join(result))