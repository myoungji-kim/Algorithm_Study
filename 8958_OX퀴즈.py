from sys import stdin
N = int(stdin.readline())
score = 0

for i in range(N):
    result = stdin.readline().rstrip()
    cal = [0]*len(result)

    for j in range(len(result)):
        if (j==0):
            if (result[j]=="O"):
                cal[j]=1
            else:
                cal[j]=0
        else :
            if (result[j-1]=="O" and result[j]=="O"):
                cal[j] = cal[j-1]+1
            elif(result[j]=="O"):
                cal[j] = 1
            else:
                cal[j] = 0
        score += cal[j]
    print(score)
    score=0