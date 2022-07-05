n = 1
nums = []
while True:
    sum = n

    for i in str(n):
        sum += int(i)

    if sum <= 10000:
        nums.append(sum)
        n += 1
    else:
        break

for i in range(9994):
    if i + 1 not in nums:
        print(i + 1)
