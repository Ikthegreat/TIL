import sys
sys.stdin = open('DFS.txt', 'r')


def dfs(s):
    stack = [s]
    visited[s] = 1
    result.append(s)

    while True:
        for e in route[s]:
            if visited[e] == 0:
                s = e
                stack.append(s)
                visited[s] = 1
                result.append(s)
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break


Test_case = int(input())

for t in range(Test_case):
    V, E = map(int, input().split())
    route = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    result = []
    for _ in range(E):
        start, end = map(int, input().split())
        route[start].append(end)
        route[end].append(start)

    for v in range(V):
        route[v].sort()

    dfs(1)

    print(f'#{t+1}', end=' ')
    print(*result)
