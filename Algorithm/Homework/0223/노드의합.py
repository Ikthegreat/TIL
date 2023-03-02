Test_case = int(input())

for t in range(Test_case):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    for _ in range(M):
        idx, d = map(int, input().split())
        tree[idx] = d

    for n in range(N, L - 1, -1):
        tree[n//2] += tree[n]  # 부모노드에 자식노드 값 누적

    result = tree[L]

    print(f'#{t+1} {result}')
