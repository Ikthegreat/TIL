import sys
sys.stdin = open('rectangle_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    X1, Y1, X2, Y2 = map(int, input().split())
    N = int(input())
    result = [0, 0, 0]
    for _ in range(N):
        X, Y = map(int, input().split())
        if (X1 <= X <= X2) and Y1 <= Y <= Y2:
            if X == X1 or X == X2 or Y == Y1 or Y == Y2:
                result[1] += 1
            else:
                result[0] += 1
        else:
            result[2] += 1

    print(f'#{t+1}', end=' ')
    print(*result)
