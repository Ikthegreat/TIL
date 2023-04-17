import sys
sys.stdin = open('supply_route.txt', 'r')

from collections import deque


def stack_bfs(si, sj):
    queue = deque()
    queue.append((si, sj))
    stack[si][sj] = arr[si][sj]

    while queue:
        ci, cj = queue.popleft()
        for di, dj in direction:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N:
                if stack[ni][nj] > stack[ci][cj] + arr[ni][nj]:
                    queue.append((ni, nj))
                    stack[ni][nj] = stack[ci][cj] + arr[ni][nj]


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [[2000] * N for _ in range(N)]
    stack_bfs(0, 0)
    result = stack[N-1][N-1]
    print(f'#{t+1} {result}')
