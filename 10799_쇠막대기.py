import sys

inputBKT = list(sys.stdin.readline())
cntOpen  = []
cntSplit = 0

for i in range(len(inputBKT)) :
    # Case 1: 여는 괄호
    if (inputBKT[i]=='(') :
        cntOpen.append(inputBKT[i])

    # Case 2: 닫는 괄호
    elif (inputBKT[i]==')') :
        cntOpen.pop()

        # Case 2-1: 직전 괄호의 여부에 따라 레이저 증가
        if (inputBKT[i-1] == ')') :
            cntSplit += 1
        else :
            cntSplit += len(cntOpen)

print(cntSplit)

