Test_case = int(input())

for t in range(Test_case):
    P = input()
    stack = []
    for i in P:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if '(' in stack:
                stack.pop()
            else:
                result = 0
                break
    if len(stack) == 0:
        result = 1
    else:
        result = 0

    print(f'#{t+1} {result}')