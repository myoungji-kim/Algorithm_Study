import sys
Repeat = int(sys.stdin.readline()) #명령 반복 횟수
Cue = []

for i in range(Repeat) :
    x = sys.stdin.readline().strip().split(' ')

    # Push
    if (x[0] == 'push') :
        Cue.append(int(x[1]))

    elif (x[0] == 'pop') :
        print('-1' if len(Cue) == 0 else Cue.pop(0))

    # Size
    elif (x[0] == 'size') :
        print(len(Cue))

    # Empty
    elif (x[0] == 'empty') :
        print('1' if len(Cue) == 0 else '0')

    # Top
    elif (x[0] == 'top') :
        print('-1' if len(Cue) == 0 else Cue[-1])

    # Front
    elif (x[0] == 'front') :
        print(Cue[0] if len(Cue) != 0 else '-1')

    # Back
    elif (x[0] == 'back') :
        print(Cue[len(Cue)-1] if len(Cue) != 0 else '-1')