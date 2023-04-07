import sys
sys.stdin = open('Group.txt', 'r')


def bfs(s):
    q = [s]
    visited[s] = 1

    while q:
        dq = q.pop(0)
        for e in cn[dq]:
            if visited[e] == 0:
                visited[e] = 1
                q.append(e)


Test_case = int(input())

for t in range(Test_case):
    N, M = map(int, input().split())
    application = list(map(int, input().split()))
    cn = [[] for _ in range(N+1)]
    visited = [0] * (N + 1)
    result = 0

    for i in range(0, M*2, 2):
        cn[application[i]].append(application[i+1])
        cn[application[i+1]].append(application[i])

    for r in range(1, N + 1):
        if visited[r] == 0:
            bfs(r)
            result += 1

    print(f'#{t+1} {result}')
