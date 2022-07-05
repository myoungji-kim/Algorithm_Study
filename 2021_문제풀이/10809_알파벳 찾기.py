import sys
from string import ascii_lowercase

# 변수 설정 (1: 입력, 2: 알파벳 리스트, 3: 알파벳 길이만큼 -1으로 된 리스트)
inputWords = list(sys.stdin.readline().rstrip())
alpha  = list(ascii_lowercase)
result = [-1]*len(alpha)

# 구현 (알파벳 겹치고 -1일 때 i 값으로 변경)
for i in range(len(inputWords)) :
    for j in range(len(alpha)) :
        if (inputWords[i] == alpha[j] and result[j] == -1) :
            result[j] = i

# 결과 출력
print(" ".join(map(str, result)))