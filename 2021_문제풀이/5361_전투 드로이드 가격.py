from sys import stdin
menu = [350.34, 230.90, 230.90, 190.55, 180.90]

for i in range(int(stdin.readline())):
    cost = 0
    for j in range(5):
        buy = list(map(int, stdin.readline().split()))
        cost += buy[j] * menu[j]
    cost = float(cost)

    print("$", "{:.2f}".format(cost), sep="")