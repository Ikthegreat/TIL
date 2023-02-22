import sys
sys.stdin = open('node_distance_input.txt', 'r')


def bfs(s, g):
    visited = [0] * (V + 1)
    queue = [s]

    visited[s] = 0
    while queue:
        t = queue.pop(0)
        for e in route[t]:
            if visited[e] == 0:
                queue.append(e)
                visited[e] = visited[t] + 1

    return visited[g]


Test_case = int(input())

for t in range(Test_case):
    V, E = map(int, input().split())
    route = [[] for _ in range(V + 1)]
    for _ in range(E):
        node1, node2 = map(int, input().split())
        route[node1].append(node2)
        route[node2].append(node1)

    S, G = map(int, input().split())

    print(f'#{t+1}', end=' ')
    print(bfs(S, G))
