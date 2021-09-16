import sys
from collections import deque

# Left : 커서 왼쪽, Right : 커서 오른쪽
Left  = deque(sys.stdin.readline().rstrip())
Right = deque([])

# 명령 반복 횟수
Repeat = int(sys.stdin.readline())

for i in range (Repeat) :
    # 어디로 이동, 무엇을 추가
    Command = sys.stdin.readline().rstrip().split(' ')

    if (Command[0]=='L' and len(Left) != 0):
        Right.appendleft(Left[-1])
        Left.pop()
    elif (Command[0]=='D' and len(Right) != 0):
        Left.append(Right[0])
        del Right[0]
    elif (Command[0]=='B' and len(Left) != 0):
        Left.pop()
    elif (Command[0]=='P'):
        Left.append(Command[1])

Result = Left+Right
print("".join(Result))