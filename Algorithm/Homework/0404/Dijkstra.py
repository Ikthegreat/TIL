import sys
sys.stdin = open('Dijkstra.txt', 'r')


def dijkstra(s):
    d = route[0][:]
    visited = [0] * N
    visited[s] = 1

    for _ in range(N-1):
        idx = 0
        temp = 100
        for j in range(N):
            if visited[j] == 0:
                if temp >= d[j]:
                    temp = d[j]
                    idx = j

        visited[idx] = 1
        for j in range(N):
            d[j] = min(d[j], d[idx] + route[idx][j])

    return d[-1]


Test_case = int(input())

for t in range(Test_case):
    N, E = map(int, input().split())
    INF = 10000
    route = [[INF] * N for _ in range(N)]
    for i in range(N):
        route[i][i] = 0
    for _ in range(E):
        start, end, distance = map(int, input().split())
        route[start][end] = distance

    result = dijkstra(0)

    print(f'#{t+1} {result}')
