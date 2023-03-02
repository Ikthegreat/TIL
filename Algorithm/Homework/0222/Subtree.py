import sys
sys.stdin = open('Subtree_input.txt', 'r')


def preorder(n):
    if n:
        result.append(n)
        preorder(ch1[n])
        preorder(ch2[n])


Test_case = int(input())

for t in range(Test_case):
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)
    result = []
    for i in range(0, len(tree), 2):
        p, c = tree[i], tree[i + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    preorder(N)

    print(f'#{t+1} {len(result)}')