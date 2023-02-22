import sys
sys.stdin = open('괄호검사2_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    string = input()
    stack = []
    for s in string:
        if s == '{':
            stack.append(s)
        elif s == '(':
            stack.append(s)
        elif s == '}':
            if '{' in stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(s)
                break
        elif s == ')':
            if '(' in stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
                break
    if len(stack) == 0:
        result = 1
    else:
        result = 0
    print(f'#{t+1} {result}')
