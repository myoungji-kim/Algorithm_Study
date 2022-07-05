import sys

inputWords = list(sys.stdin.readline().rstrip())
suffix = []

# 1: 접미사 리스트 생성
while (len(inputWords)>0) :
    bin = "".join(inputWords)
    suffix.append(bin)
    inputWords.pop(0)

# 2: 정렬 변경
suffix.sort()

for i in range(len(suffix)) :
    print(suffix[i])

