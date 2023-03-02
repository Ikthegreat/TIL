import sys
sys.stdin = open()


def postord(n):
    if tree[n]:  # 노드가 존재하는 경우 처리
        if tree[n] == '+'
    else:

Test_case = 10

for t in range(Test_case):
    N = int(input())
    tree, left, right = [[0] * (N + 1) for _ in range(3)]
    for _ in range(N):
        temp = input().split()
        idx = int(temp[0])
        tree[idx] = temp[1]
        if len(temp) > 2:
            left[idx] = int(temp[2])
            right[idx] = int(temp[3])