import sys

# 임의의 여러줄 입력 받기
while True:
    A, B = map(int, sys.stdin.readline().split())
    cnt = [0] * 4

    # 종료
    if (A==0 and B==0):
        break

    # 결과 출력
    print(A+B)