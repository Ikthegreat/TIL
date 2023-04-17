Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    check = [[0] * 10 for _ in range(10)]
    result = 0
    for n in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                check[i][j] += color
                if check[i][j] == 3:
                    result += 1
    print(f'#{t+1} {result}')