import sys
sys.stdin = open('Forth_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    string = input().split()
    ys = ['+', '-', '*', '/', '.']
    for i in range(len(string)):
        if string[i] in ys:
            string[i] = string[i]
        else:
            string[i] = int(string[i])

    stack = []
    for s in string:
        if s == '.':
            if len(stack) == 1:
                result = stack.pop()
                break
            else:
                result = 'error'
                break

        elif type(s) == int:
            stack.append(s)

        else:
            if len(stack) >= 2:
                if s == '+':
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 + num2)

                elif s == '-':
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 - num2)

                elif s == '*':
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 * num2)

                elif s == '/':
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 // num2)

            else:
                result = 'error'
                break

    print(f'#{t+1} {result}')
