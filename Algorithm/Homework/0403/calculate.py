from collections import deque
import sys
sys.stdin = open('calculate.txt', 'r')

def bfs(s):
    queue = deque()
    queue.append((s, 0))
    visited[s] = 1

    while queue:
        e, count = queue.popleft()
        if e == M:
            return count

        a = e+1
        b = e-1
        c = e*2
        d = e-10

        if (0 < a <= 1000000) and visited[a] == 0:
            queue.append((a, count+1))
            visited[a] = 1
        if (0 < b <= 1000000) and visited[b] == 0:
            queue.append((b, count+1))
            visited[b] = 1
        if (0 < c <= 1000000) and visited[c] == 0:
            queue.append((c, count+1))
            visited[c] = 1
        if (0 < d <= 1000000) and visited[d] == 0:
            queue.append((d, count+1))
            visited[d] = 1


Test_case = int(input())

for t in range(Test_case):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    result = bfs(N)

    print(f'#{t+1} {result}')
