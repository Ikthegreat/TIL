import sys
sys.stdin = open('길찾기_input.txt', 'r')

Test_case = 10
Start, End = 0, 99
V = 99


def DFS_stack(num):
    visited = [0] * (V+1)
    stack = []
    start = num
    visited[start] = 1
    path.append(start)

    while True:
        for end in range(1, V+1):
            if visited[end] == 0 and adj[start][end]:
                stack.append(start)
                start = end
                visited[start] = 1
                path.append(start)
                break
        else:
            if stack:
                start = stack.pop()
            else:
                break


for t in range(Test_case):
    T, E = map(int, input().split())
    data = list(map(int, input().split()))
    adj = [[0] * (V+1) for _ in range(V+1)]

    for i in range(0, E*2-1, 2):
        s = data[i]
        e = data[i+1]

        for _ in range(E):
            adj[s][e] = adj[s][e] = 1

    path = []
    DFS_stack(Start)

    if End in path:
        result = 1
    else:
        result = 0
    print(f'#{t+1}', result)