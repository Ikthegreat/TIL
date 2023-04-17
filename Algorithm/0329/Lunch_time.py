from collections import deque
import sys
sys.stdin = open('Lunch_time.txt', 'r')


def c(ti, tj):
    global visited1
    for ti in range(N):
        for tj in range(N):
            if room[ti][tj] == 1:
                    people1.append(visited[ti][tj])
                else:
                    people2.append(visited[ti][tj])


def bfs(d, si, sj):
    queue = deque([(d, si, sj)])
    visited[si][sj] = d

    while queue:
        (d, ci, cj) = queue.popleft()
        for mi, mj in direction:
            ni, nj = ci + mi, cj + mj
            if 0 <= ni < N and 0 <= nj < N and (visited[ni][nj] == 0):
                visited[ni][nj] = visited[ci][cj] + 1
                queue.append((d, ni, nj))

    for n in range(N):
        print(visited[n])
    print()


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    stair = []
    people1 = []
    people2 = []
    visited1 = [[0] * N for _ in range(N)]
    visited2 = [[0] * N for _ in range(N)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(N):
        for j in range(N):
            if room[i][j] and room[i][j] != 1:
                stair.append((room[i][j], i, j))

    for s in range(2):
        bfs(stair[s][0], stair[s][1], stair[s][2])

room.sort()