import sys
sys.stdin = open('calc_input.txt', 'r')

Test_case = 10

for t in range(Test_case):
    N = int(input())
    string = input()

    operator = []
    stack = []
    for s in string:
        if s != '+':
            stack.append(int(s))
        else:
            while operator:
                stack += operator.pop()
            operator += s

    while operator:
        stack.append(operator.pop())

    print(stack)

    result = []
    for i in stack:
        if type(i) == int:
            result.append(i)
        else:
            if len(result) >= 2:
                num2 = result.pop()
                num1 = result.pop()
                result.append(num1 + num2)

    print(f'#{t+1}', end=' ')
    print(*result)
