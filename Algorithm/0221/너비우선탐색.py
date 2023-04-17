import sys
sys.stdin = open('bfs_input.txt', 'r')


def bfs(s, N):
    visited = [0] * (N + 1)
    queue = [s]
    visited[s] = 1

    while queue:
        dequeue = queue.pop(0)
        result.append(dequeue)
        for e in route[dequeue]:
            if visited[e] == 0:
                queue.append(e)
                visited[e] = visited[dequeue] + 1


Test_case = int(input())

for t in range(Test_case):
    V, E = map(int, input().split())
    route = [[] for _ in range(V+1)]
    result = []
    for _ in range(E):
        start, end = map(int, input().split())
        route[start].append(end)
        route[end].append(start)

    bfs(1, V)

    print(f'#{t+1}', end=' ')
    print(*result)
