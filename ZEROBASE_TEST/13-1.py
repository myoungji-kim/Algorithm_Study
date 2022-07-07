def solution(nums):
    numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer = 0
    isMinus, hasSign = False, True
    maxNum, minNum = 2 ** 31 - 1, -2 ** 31 + 1

    nums = nums.lstrip()

    if nums[0] == '-':
        isMinus = True
    elif nums[0] != '+':
        hasSign = False

    if hasSign:
        nums = nums[2:]
        nums = nums.lstrip()

    for n in nums:
        if n in numList:
            answer = answer * 10 + int(n)
        else:
            break

    if isMinus:
        answer *= -1

    if answer > maxNum:
        answer = maxNum
    elif answer < minNum:
        answer = minNum

    return answer


print(solution("+ 43530432 4324"))
