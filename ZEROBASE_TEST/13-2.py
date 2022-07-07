def solution(arr, target):
    arr.sort()
    answer = 99999999

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                temp = target - (arr[i] + arr[j] + arr[k])
                if abs(temp) < abs(answer):
                    answer = temp
                elif abs(temp) == abs(answer):
                    if temp > 0:
                        answer = temp

    return target - answer


# 20
print(solution([2, 3, 5, 10, 12, 15], 21))
