import sys
sys.stdin = open('leejin_input.txt', 'r')


def inorder(n):
    if n:
        inorder(ch1[n])
        result.append(n)
        inorder(ch2[n])


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    nums = list(range(2, N + 1))
    tree = []
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    result = []
    for i in range(len(nums)):
        tree.append(nums[i]//2)
        tree.append(nums[i])

    for j in range(0, len(tree), 2):
        p, c = tree[j], tree[j+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    inorder(1)

    for k in range(len(result)):
        if result[k] == 1:
            root = k + 1
        elif result[k] == N // 2:
            answer = k + 1

    print(f'#{t+1} {root} {answer}')