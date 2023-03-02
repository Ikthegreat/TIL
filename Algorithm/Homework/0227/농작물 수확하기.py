import sys
sys.stdin = open('농작물.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start = mid = end = N // 2
    count = 0
    for i in range(N):
        for j in range(start, end + 1):
            count += arr[i][j]
        if i < mid:
            start -= 1
            end += 1
        elif i >= mid:
            start += 1
            end -= 1

    print(f'#{t+1} {count}')
