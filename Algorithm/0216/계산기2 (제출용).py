import sys
sys.stdin = open('calc_input.txt', 'r')

Test_case = 10

operator = {'+': 1, '*': 2}

for t in range(Test_case):
    N = int(input())
    string = list(input())
    postfix = []
    stack = []
    for idx in range(len(string)):
        if string[idx] in operator:
            if stack:
                while stack and operator[stack[-1]] >= operator[string[idx]]:
                    postfix.append(stack.pop())
                stack.append(string[idx])
            else:
                stack.append(string[idx])
        else:
            postfix.append(int(string[idx]))

    while stack:
        postfix.append(stack.pop())

    result = []
    for P in postfix:
        if type(P) == int:
            result.append(P)
        else:
            if operator[P] == 1:
                num2 = result.pop()
                num1 = result.pop()
                result.append(num1 + num2)
            else:
                num2 = result.pop()
                num1 = result.pop()
                result.append(num1 * num2)

    print(f'#{t+1}', end=' ')
    print(*result)

