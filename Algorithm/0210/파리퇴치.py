import sys
sys.stdin = open('파리퇴치_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    weapon = [0] * M
    catch = [[0] * (N - M + 1) for _ in range(N - M + 1)]
    result = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            count = 0
            for k in range(j, j+M):
                weapon[k-j] = fly[k][i:i+M]
            for x in range(len(weapon)):
                for y in range(len(weapon)):
                    count += weapon[x][y]
            catch[i][j] = count
            if result <= count:
                result = count
    print(f'#{t+1} {result}')


