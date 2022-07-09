from sys import stdin

N = int(stdin.readline())
for i in range(N):
    word = stdin.readline().rstrip().lower()
    while len(word) > 1:
        if word[0] != word[-1]:
            res = 'NO'
            break
        word = word[1:-1]
    else:
        res = 'YES'

    print("#", i + 1, sep="", end=" ")
    print(res)

# Case 2
# word == word[::-1] 이러면 초간단하게 해결..