import sys
sys.stdin = open('calculate_input.txt', 'r')


def order(n):
    if n:
        order(left[n])
        order(right[n])
        result.append(tree[n])


Test_case = 10

for t in range(Test_case):
    N = int(input())
    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for n in range(N):
        node = list(map(str, input().split()))
        for i in range(len(node)):
            if node[i] not in ['+', '-', '*', '/']:
                node[i] = int(node[i])

        tree[node[0]] = node[1]
        if len(node) > 2:
            if left[node[0]] == 0:
                left[node[0]] = node[2]
            if left[node[0]] != 0:
                right[node[0]] = node[3]

    result = []
    order(1)

    stack = []
    for s in result:
        if type(s) == int:
            stack.append(s)
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if s == '+':
                stack.append(num1 + num2)
            elif s == '-':
                stack.append(num1 - num2)
            elif s == '*':
                stack.append(num1 * num2)
            elif s == '/':
                stack.append(num1 / num2)

    print(f'#{t+1}', end=' ')
    print(int(*stack))
