import sys
from string import ascii_lowercase

# 변수 설정 (1: 입력, 2: 알파벳 리스트, 3: 알파벳 길이만큼 0으로 된 리스트)
inputWords = list(sys.stdin.readline().rstrip())
alpha  = list(ascii_lowercase)
result = [0]*len(alpha)

# 구현 (알파벳 겹칠 때마다 result 리스트 해당 부분에 +1)
for i in range(len(inputWords)) :
    for j in range(len(alpha)) :
        if (inputWords[i] == alpha[j]) :
            result[j] += 1

# 결과 출력
print(" ".join(map(str, result)))