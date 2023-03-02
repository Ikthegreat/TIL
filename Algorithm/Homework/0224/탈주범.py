import sys
sys.stdin = open('탈주범_input.txt', 'r')


def bfs(start_i, start_j, time):
    queue = [(start_i, start_j)]

    visited[start_i][start_j] = 1

    while queue:
        current_i, current_j = queue.pop(0)

        if underground[current_i][current_j] == 1:
            for move_i, move_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_i, next_j = current_i + move_i, current_j + move_j
                if (0 <= next_i < N) and (0 <= next_j < M) and visited[next_i][next_j] == 0 and underground[next_i][next_j] != 0:
                    visited[next_i][next_j] = visited[current_i][current_j] + 1
                    queue.append((next_i, next_j))
        elif underground[current_i][current_j] == 2:
            for move_i, move_j in [(-1, 0), (1, 0)]:
                next_i, next_j = current_i + move_i, current_j + move_j
                if (0 <= next_i < N) and (0 <= next_j < M) and visited[next_i][next_j] == 0 and underground[next_i][next_j] != 0:
                    visited[next_i][next_j] = visited[current_i][current_j] + 1
                    queue.append((next_i, next_j))
        elif underground[current_i][current_j] == 3:
            for move_i, move_j in [(0, -1), (0, 1)]:
                next_i, next_j = current_i + move_i, current_j + move_j
                if (0 <= next_i < N) and (0 <= next_j < M) and visited[next_i][next_j] == 0 and underground[next_i][next_j] != 0:
                    visited[next_i][next_j] = visited[current_i][current_j] + 1
                    queue.append((next_i, next_j))
        elif underground[current_i][current_j] == 4:
            for move_i, move_j in [(-1, 0), (0, 1)]:
                next_i, next_j = current_i + move_i, current_j + move_j
                if (0 <= next_i < N) and (0 <= next_j < M) and visited[next_i][next_j] == 0 and underground[next_i][next_j] != 0:
                    visited[next_i][next_j] = visited[current_i][current_j] + 1
                    queue.append((next_i, next_j))
        elif underground[current_i][current_j] == 5:
            for move_i, move_j in [(1, 0), (0, 1)]:
                next_i, next_j = current_i + move_i, current_j + move_j
                if (0 <= next_i < N) and (0 <= next_j < M) and visited[next_i][next_j] == 0 and underground[next_i][next_j] != 0:
                    visited[next_i][next_j] = visited[current_i][current_j] + 1
                    queue.append((next_i, next_j))
        elif underground[current_i][current_j] == 6:
            for move_i, move_j in [(1, 0), (0, -1)]:
                next_i, next_j = current_i + move_i, current_j + move_j
                if (0 <= next_i < N) and (0 <= next_j < M) and visited[next_i][next_j] == 0 and underground[next_i][next_j] != 0:
                    visited[next_i][next_j] = visited[current_i][current_j] + 1
                    queue.append((next_i, next_j))
        elif underground[current_i][current_j] == 7:
            for move_i, move_j in [(-1, 0), (0, -1)]:
                next_i, next_j = current_i + move_i, current_j + move_j
                if (0 <= next_i < N) and (0 <= next_j < M) and visited[next_i][next_j] == 0 and underground[next_i][next_j] != 0:
                    visited[next_i][next_j] = visited[current_i][current_j] + 1
                    queue.append((next_i, next_j))


Test_case = int(input())

for t in range(Test_case):
    N, M, R, C, L = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    bfs(R, C, L)
    count = 0
    for i in range(N):
        for j in range(M):
            if 1 <= visited[i][j] <= L:
                count += 1

    for i in range(N):
        print(visited[i])

    print(count)