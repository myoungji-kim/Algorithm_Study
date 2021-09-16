import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n) :
    x =  sys.stdin.readline().strip().split(' ')
    if x[0] == 'push' :
        stack.append(int(x[1]))
    elif x[0] == 'pop' :
        if len(stack) == 0 :
            print('-1')
        else :
            print(stack.pop())
    elif x[0] == 'size' :
        print(len(stack))
    elif x[0] == 'empty' :
        if len(stack) == 0 :
            print('1')
        else :
            print('0')
    elif x[0] == 'top' :
        if len(stack) == 0 :
            print('-1')
        else :
            print(stack[-1])