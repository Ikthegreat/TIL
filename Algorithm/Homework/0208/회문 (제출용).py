Test_case = int(input())

for t in range(Test_case):
    N, M = map(int, input().split())
    string = [input() for _ in range(N)]
    for n in range(N):
        for i in range(N - M + 1):
            horizontal = string[n][i:(i+M)]
            vertical = string[i:(i+M)][n]
            if horizontal == horizontal[::-1]:
                result = horizontal
                break
            elif vertical == vertical[::-1]:
                result = vertical
                break
            else:
                continue

    print(result)




