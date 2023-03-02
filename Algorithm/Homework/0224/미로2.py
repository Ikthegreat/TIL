import sys
sys.stdin = open('maze2_input.txt', 'r')


def bfs(idx_i, idx_j):
    visited = [[0] * 100 for _ in range(100)]
    queue = [(idx_i, idx_j)]
    visited[idx_i][idx_j] = 1

    while queue:
        current_i, current_j = queue.pop(0)
        if (current_i, current_j) == (end_i, end_j):
            return 1
        for move_i, move_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_i, next_j = current_i + move_i, current_j + move_j
            if (0 <= next_i < 100) and (0 <= next_j < 100) and (maze[next_i][next_j] != 1) and (visited[next_i][next_j] == 0):
                visited[next_i][next_j] = visited[current_i][current_j] + 1
                queue.append((next_i, next_j))
    else:
        return 0


Test_case = 10

for t in range(Test_case):
    _ = int(input())
    maze = [list(map(int, input())) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                start_i, start_j = i, j
            elif maze[i][j] == 3:
                end_i, end_j = i, j

    print(f'#{t+1}', end=' ')
    print(bfs(start_i, start_j))

