import sys
sys.stdin = open('러시아국기.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    color_list = [[0] * 3 for _ in range(N)]
    count = 0
    result = []
    for i in range(N):
        for j in range(M):
            if flag[i][j] == 'W':
                color_list[i][0] += 1
            elif flag[i][j] == 'B':
                color_list[i][1] += 1
            else:
                color_list[i][2] += 1

    count += color_list[0][1] + color_list[0][2] + color_list[N - 1][0] + color_list[N - 1][1]

    start = 1
    end = N - 2
    while True:
        if color_list[start][0] >= color_list[start][1]:
            count += sum(color_list[start]) - color_list[start][0]
            start += 1
        else:
            break
        if start + 1 >= end:
            if color_list[start][0] > color_list[start][1]:
                count += sum(color_list[start]) - color_list[start][0]
                start += 1
            break

    while True:
        if color_list[end][2] >= color_list[end][1]:
            count += sum(color_list[end]) - color_list[end][2]
            end -= 1
        else:
            break
        if start + 1 >= end:
            break

    for i in range(start, end + 1):
        count += color_list[i][0] + color_list[i][2]

    print(f'#{t+1} {count}')
