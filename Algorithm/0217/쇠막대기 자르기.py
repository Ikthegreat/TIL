Test_case = int(input())

for t in range(Test_case):
    string = input()
    result = count = 0
    for i in range(len(string)):
        if string[i] == '(':           # 막대기 시작 또는 레이저 시작
            count += 1
        else:                          # 바로 앞의 기호를 확인
            if string[i-1] == '(':     # 레이저
                count -= 1
                result += count
            else:                      # 막대기의 끝
                count -= 1
                result += 1

    print(f'#{t+1} {result}')