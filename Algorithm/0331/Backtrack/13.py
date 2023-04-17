import sys
sys.stdin = open('13.txt', 'r')


def cal(a, b):  # 같은 재료는 어차피 0 이므로 모든 조합 다 처리
    s1 = s2 = 0
    for i in range(M):
        for j in range(M):
            s1 += table[a[i]][a[j]]
            s2 += table[b[i]][b[j]]
    return abs(s1 - s2)


def dfs(n, temp1, temp2):
    global result
    if n == N:
        if len(temp1) == M:
            result = min(result, cal(temp1, temp2))
        return

    # 요리 1 선택한 경우
    dfs(n+1, temp1 + [n], temp2)
    # 요리 2 선택한 경우
    dfs(n+1, temp1, temp2 + [n])


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    M = N // 2
    result = N * N * 20000
    dfs(0, [], [])

    print(f'#{t + 1} {result}')
