import sys
sys.stdin = open('maze_distance_input.txt', 'r')


def bfs(idx_i, idx_j):
    visited = [[0] * N for _ in range(N)]
    queue = []
    result = 0

    visited[idx_i][idx_j] = 1
    queue.append((idx_i, idx_j))

    while queue:
        current_i, current_j = queue.pop(0)

        for move_i, move_j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_i = current_i + move_i
            next_j = current_j + move_j
            if (0 <= next_i < N) and (0 <= next_j < N) and maze[next_i][next_j] == 0 and visited[next_i][next_j] == 0:
                queue.append((next_i, next_j))
                visited[next_i][next_j] = visited[current_i][current_j] + 1
        if (current_i, current_j) == (end_i, end_j):
            result = visited[current_i][current_j] - 2
            return result

    return result


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            maze[i][j] = int(maze[i][j])
            if maze[i][j] == 2:
                start_i, start_j = i, j
            elif maze[i][j] == 3:
                end_i, end_j = i, j
                maze[i][j] = 0

    print(f'#{t+1}', end=' ')
    print(bfs(start_i, start_j))