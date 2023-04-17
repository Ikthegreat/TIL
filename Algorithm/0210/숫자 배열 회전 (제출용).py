Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]

    result = [[0] * 3 for _ in range(N)]
    for repeat in range(3):
        for i in range(N):
            for j in range(N):
                if i < j:
                    num[i][j], num[j][i] = num[j][i], num[i][j]
            num[i] = num[i][::-1]
            temp = ''.join(list(map(str, num[i])))
            result[i][repeat] = temp

    print(f'#{t + 1}')

    for n in range(N):
        print(*result[n])
