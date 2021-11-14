from sys import stdin

length = int(stdin.readline())
heights = list(map(int, stdin.readline().split()))
start = heights[0]
results = []
for i in range(1, len(heights)):
    if heights[i - 1] >= heights[i]:
        end = heights[i - 1]
        results.append(end - start)
        start = heights[i]

    if i == len(heights) - 1 and heights[i - 1] < heights[i]:
        end = heights[i]
        results.append(end - start)

print(max(results))
