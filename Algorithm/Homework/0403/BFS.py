import sys
sys.stdin = open('BFS.txt', 'r')


def bfs(s):
    queue = [s]
    visited[s] = 1

    while queue:
        dequeue = queue.pop(0)
        result.append(dequeue)
        for d in route[dequeue]:
            if visited[d] == 0:
                queue.append(d)
                visited[d] = 1


Test_case = int(input())

for t in range(Test_case):
    V, E = map(int, input().split())
    route = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    result = []
    for e in range(E):
        start, end = map(int, input().split())
        route[start].append(end)
        route[end].append(start)

    for v in range(V):
        route[v].sort()

    bfs(1)

    print(f'#{t+1}', end=' ')
    print(*result)
