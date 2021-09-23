from sys import stdin

while True:
    num = stdin.readline()
    Flag = True

    if int(num) == 0:
        exit()
    else:
        for i in range(len(num)//2):
            if num[i] != num[len(num)-i-2]:
                Flag = False
                break
        print("yes") if Flag else print("no")