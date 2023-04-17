import sys
sys.stdin = open('길찾기_input.txt', 'r')


def DFS(start):
    stack = []  # 필요한 배열 flag, 변수 생성

    s = start
    v[s] = 1    # 시작 위치에서의 방문 표시 등

    while True:
        for e in temp[s]:        # 연결된 노드 하나씩 처리
            if v[e] == 0:        # 미방문인 경우
                stack.append(s)  # 돌아오기위해 기준점 push

                s = e
                v[s] = 1
                break
        else:
            if stack:
                s = stack.pop()  # 현 기준점에서 더 이상 탐색할 위치가 없을 경우
            else:
                break


for _ in range(10):
    Test_case, E = map(int, input().split())
    path = list(map(int, input().split()))
    N = 100  # 0 ~ 99 고정
    temp = [[] for _ in range(N)]
    for p in range(0, len(path), 2):
        s, e = path[p], path[p+1]
        temp[s].append(e)

    S, G = 0, 99
    v = [0] * N
    DFS(S)
    print(f'#{Test_case} {v[G]}')
