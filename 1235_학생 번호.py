from sys import stdin

student = []
check = []
answer = 0

for i in range(int(stdin.readline())):
    student.append(stdin.readline().rstrip())

for i in range(len(student[0])-1, -1, -1):
    for j in range(len(student)):
        check.append(student[j][i])

    if sorted(list(set(check))) != sorted(check):
        answer += 1
        check = []

        if len(student) == answer:
            print(answer)
            exit()
    else:
        break

print(answer)