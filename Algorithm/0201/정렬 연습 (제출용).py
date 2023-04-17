Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    num = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

    str_num = (' '.join(list(map(str, num))))

    print(f'#{t+1} {str_num}')