import sys
sys.stdin = open('16.txt', 'r')


def eat(a, b, idx, eaten):
    global result, i, j

    if a == i and b == j and idx == 3:
        result = max(result, len(eaten))
        return

    if 0 <= a < N and 0 <= b < N and dessert[a][b] not in eaten:
        eaten += [dessert[a][b]]

    eat(a+direction[idx][0], b+direction[idx][1], idx, eaten)

    if idx < 3:
        eat(a+direction[idx+1][0], b+direction[idx+1][1], idx+1, eaten)


Test_case = int(input())

for t in range(2):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    direction = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    for i in range(N):
        for j in range(1, N-1):
            eat(i, j, 0, [])
    print(f'#{t+1} {result}')
