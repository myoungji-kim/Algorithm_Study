from sys import stdin

name1 = list(stdin.readline().rstrip())
name2 = list(stdin.readline().rstrip())
nums = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
test = [[]]
for i in range(len(name1)):
    test[0].append(nums[ord(name1[i]) - 65])
    test[0].append(nums[ord(name2[i]) - 65])

while True:
    test.append([])
    for i in range(len(test[-2]) - 1):
        test[-1].append((test[-2][i] + test[-2][i + 1]) % 10)

    if len(test[-1]) == 2:
        break
print(str(test[-1][0])+str(test[-1][1]))