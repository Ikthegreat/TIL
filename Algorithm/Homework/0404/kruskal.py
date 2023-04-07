import sys
sys.stdin = open('kruskal.txt', 'r')


def find_set(n):
    if n == p[n]:
        return n
    p[n] = find_set(p[n])
    return p[n]


def union(s, e):
    p[find_set(e)] = find_set(s)


def kruskal():
    # [1] 링크 중심의 처리 w 값 기준으로 오름차순 정렬
    arr.sort(key=lambda x: x[2])

    # [2] v 개의 링크를 선택 (같은 그룹이 아닌 경우에만 선택)
    count = rt = 0
    for (s, e, w) in arr:
        # s, e 가 연결되어 있지 않은 경우 (사이클이 아닌 경우)
        if find_set(s) != find_set(e):
            union(s, e)
            count += 1
            rt += w
            if count == V:
                return rt

    return -1


Test_case = int(input())

for t in range(Test_case):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    # [1] make_set() : 각자가 대표인 그룹 생성
    p = [n for n in range(V+1)]

    result = kruskal()
    print(f'#{t+1} {result}')
