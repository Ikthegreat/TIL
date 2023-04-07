import sys
sys.stdin = open('kruskal.txt', 'r')


def prim(s):
    visited[s] = 1
    rt = 0

    for _ in range(V):
        ''

INF = 1000000
Test_case = int(input())

for t in range(Test_case):
    V, E = map(int, input().split())
    arr = [[INF] * (V+1) for _ in range(V+1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        start, end, weight = map(int, input().split())
        arr[start][end] = weight
        arr[end][start] = weight

    result = prim(0)

    print(f'#{t+1} {result}')