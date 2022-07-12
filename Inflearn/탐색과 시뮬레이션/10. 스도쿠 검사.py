from sys import stdin


def check(a):
    # 가로, 세로줄 체크
    for i in range(9):
        ch1 = [0] * 10  # 행
        ch2 = [0] * 10  # 열
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) + sum(ch2) != 18:
            return False

    # 그룹 네모 체크
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                return False
    return True


sdocu = [list(map(int, stdin.readline().split())) for _ in range(9)]
if check(sdocu):
    print('YES')
else:
    print('NO')