def paper(num):
    if num < 2:
        return num
    elif num == 2:
        return 3
    else:
        return paper(num - 2) * 2 + paper(num - 1)


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    N = N // 10

    print(f'#{t+1} {paper(N)}')

