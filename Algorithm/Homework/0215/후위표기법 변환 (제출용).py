import sys
sys.stdin = open('후위표기법_input.txt', 'r')

Test_case = int(input())

py = list(map(str, list(range(0, 10))))
ys = ['+', '*']

for t in range(Test_case):
    string = input()
    result = []
    stack = []
    for s in string:
        if s in py:
            result.append(s)
        else:
            if stack:
                if (s == '*') and ('+' in stack):
                    if len(stack) == 2:
                        result.append(stack.pop())
                        stack.append(s)
                    else:
                        stack.append(s)
                else:
                    if len(stack) == 2:
                        while True:
                            if len(stack) == 0:
                                stack.append(s)
                                break
                            result.append(stack.pop())
                    else:
                        result.append(stack.pop())
                        stack.append(s)
            else:
                stack.append(s)
    while stack:
        result.append(stack.pop())

    result = ''.join(list(map(str, result)))

    print(f'#{t+1} {result}')
