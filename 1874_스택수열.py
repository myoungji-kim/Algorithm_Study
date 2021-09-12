import sys
Repeat = int(sys.stdin.readline())

Add = 1
Stack = []
Result = []
Bool = 'Yes'

for i in range(Repeat) :
    Num = int(sys.stdin.readline())

    # Case 1 : Push // 를 하면 무조건 Pop 을 한번은 함
    while (Add <= Num):
        Result.append('+')
        Stack.append(Add)
        Add += 1

    # Case 2 : Pop
    if (Stack[-1] == Num) :
        Stack.pop()
        Result.append('-')

    # Case 3 : False
    else :
        Bool = 'No'

if (Bool == 'No') :
    print('NO')

else :
    for i in range(len(Result)) :
        print(Result[i])

