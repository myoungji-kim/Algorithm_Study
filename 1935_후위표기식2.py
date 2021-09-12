import sys

inputRepeat = int(sys.stdin.readline().rstrip())
inputFormula = sys.stdin.readline().rstrip()
num = []
result = []
cntAlpha = 65

# 1 : 숫자 넣어줌
for i in range(inputRepeat):
    num.append(int(sys.stdin.readline().rstrip()))

# 2 : 알파벳과 연결 + 계산
for j in inputFormula:
    if (j.isalpha()):
        result.append(num[ord(j) - ord('A')])
    else:
        result.append(j)
        result[-3] = str(eval(str(result[-3])+result[-1]+str(result[-2])))
        for x in range(2): result.pop()

print("%.2f" % float(result[0]))