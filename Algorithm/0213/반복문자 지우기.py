import sys
sys.stdin = open('반복문자_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    string = list(input())
    stack = []
    for s in string:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    result = len(stack)
    print(f'#{t+1} {result}')
