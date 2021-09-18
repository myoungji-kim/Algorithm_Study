import sys
inputWords = list(sys.stdin.readline().rstrip())

for i in range(len(inputWords)) :
    # 대/소문자 판별
    if (inputWords[i].islower()) :
        if (ord(inputWords[i])<110) :
            inputWords[i] = chr(ord(inputWords[i])+13)
        else :
            inputWords[i] = chr(ord(inputWords[i])-13)

    elif (inputWords[i].isupper()) :
        if (ord(inputWords[i]) < 78):
            inputWords[i] = chr(ord(inputWords[i])+13)
        else:
            inputWords[i] = chr(ord(inputWords[i])-13)

    else :
        continue

print("".join(inputWords))
