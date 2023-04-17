import sys
sys.stdin = open('Tree_input.txt', 'r')

Test_case = int(input())


def preorder(n):
    if n:             # 존재하는 노드라면 처리
        result.append(n)  # 방문 : 필요한 처리
        preorder(ch1[n])  # 왼쪽 노드
        preorder(ch2[n])  # 오른쪽 노드


for t in range(Test_case):
    V = int(input())
    nums = list(map(int, input().split()))
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    for i in range(0, len(nums), 2):
        parent, child = nums[i], nums[i+1]
        if ch1[parent] == 0:
            ch1[parent] = child
        else:
            ch2[parent] = child

    result = []

    preorder(1)

    print(f'#{t+1}', end=' ')
    print(*result)