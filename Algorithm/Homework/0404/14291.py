import sys
sys.stdin = open('14291.txt', 'r')

from collections import deque


def bfs(si, sj):
    queue = deque()
    queue.append((si, sj))
    route[si][sj] = 0

    while queue:
        ci, cj = queue.popleft()
        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N:
                incline = 0
                if fuel_data[ni][nj] - fuel_data[ci][cj] > 0:
                    incline = fuel_data[ni][nj] - fuel_data[ci][cj]
                if route[ni][nj] > route[ci][cj] + incline + 1:
                    route[ni][nj] = route[ci][cj] + incline + 1
                    queue.append((ni, nj))

    return route[-1][-1]


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    fuel_data = [list(map(int, input().split())) for _ in range(N)]
    INF = 1000000000
    route = [[INF] * N for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    result = bfs(0, 0)

    print(f'#{t+1} {result}')
