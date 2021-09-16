Row = int(input())

for i in range(Row):
    Sentence = input().split()

    for j in range(len(Sentence)):
        Words = Sentence[j]
        print(Words[::-1], end=' ')