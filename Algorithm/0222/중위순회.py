import sys
sys.stdin = open('joong_input.txt', 'r')


def inorder(n):
    if n:
        inorder(ch1[n])
        result.append(n)
        inorder(ch2[n])


Test_case = 10

for t in range(Test_case):
    E = int(input())
    nums = list(range(2, E + 1))
    tree = []
    word = {}
    result = []
    for e in range(E):
        temp = list(map(str, input().split()))
        word[int(temp[0])] = temp[1]

    for i in range(len(nums)):
        tree.append(nums[i] // 2)
        tree.append(nums[i])

    ch1 = [0] * (E + 1)
    ch2 = [0] * (E + 1)

    for j in range(0, len(tree), 2):
        p, c = tree[j], tree[j+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    inorder(1)

    for k in range(len(result)):
        result[k] = word[result[k]]

    print(f'#{t+1}', end=' ')
    print(''.join(result))
