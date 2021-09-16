import sys
N, K = map(int, sys.stdin.readline().rstrip().split(' '))
Del = K-1      # 삭제할 위치
People = []         # 생존
NewPeople = []      # 제거 순서

for i in range(N): People.append(i+1)  # 리스트 만들기

while(len(People)>0) :
    if (len(People) <= Del) :
        Del = Del % len(People)

    NewPeople.append(People[Del])
    del People[Del]
    Del += K - 1

print('<', end='')
print(", ".join(map(str, NewPeople)), end='>')