import sys
from collections import deque

Repeat = int(sys.stdin.readline())
Deque = deque([])

for i in range(Repeat) :
    x = sys.stdin.readline().strip().split(' ')

    # Push
    if (x[0] == 'push_front') :
        Deque.appendleft(int(x[1]))

    elif (x[0] == 'push_back') :
        Deque.append(int(x[1]))

    # Pop
    elif (x[0] == 'pop_front') :
        print('-1' if len(Deque) == 0 else Deque.popleft())

    elif (x[0] == 'pop_back') :
        print('-1' if len(Deque) == 0 else Deque.pop())

    # Size
    elif (x[0] == 'size') :
        print(len(Deque))

    # Empty
    elif (x[0] == 'empty') :
        print('1' if len(Deque) == 0 else '0')

    # Front
    elif (x[0] == 'front') :
        print(Deque[0] if len(Deque) != 0 else '-1')

    # Back
    elif (x[0] == 'back') :
        print(Deque[len(Deque)-1] if len(Deque) != 0 else '-1')