import sys
Num = int(sys.stdin.readline())
Result = ' '

for i in range(Num):
    List = list(input())

    for a in range(len(List)) :
        if (List[a] != '(' and List[a] != ')') : # 괄호 이외의 문자
            Result = 'NO'
            break

    if ('(' in List[0]) : # '(' 로 시작 O
        while (List.count('(') != 0): # '('의 개수가 0이 될 때까지
            Num_1 = List.count('(')
            Num_2 = List.count(')')

            if (Num_1 == Num_2): # '('와 ')'의 개수가 같을 때
                First = List.index('(')
                Check = ')' in List[First:]
                if (Check == True): # '(' 뒤에 오는 ')' 찾아서 한꺼번에 삭제
                    Second = List.index(')')
                    del List[First], List[Second-1]
                else: # '(' 뒤에 오는 ')' 없으면 오류
                    Result = 'NO'
                    break
            else: # '('와 ')'의 개수가 다를 때
                Result = 'NO'
                break

        if (len(List) == 0) :
            Result = 'YES'

    else : # '(' 로 시작X
        Result = 'NO'

    print(Result)