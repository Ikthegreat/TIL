import sys
sys.stdin = open('spaceship_input.txt', 'r')


def check(arr, row, col):
    global result
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if arr[row][col] > arr[r][c]:
                count += 1
        if count >= 4:
            result += 1
            break


Test_case = int(input())

for t in range(Test_case):
    N, M = map(int, input().split())
    mars = [[10] * (M + 2)] + [[10] + list(map(int, input().split())) + [10] for _ in range(N)] + [[10] * (M + 2)]
    result = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            check(mars, i, j)

    print(f'#{t+1} {result}')
