import sys
sys.stdin = open('깊이우선탐색_input.txt', 'r')

Test_case = int(input())
for t in range(Test_case):
    V, E = map(int, input().split())
    stack = [1]
    for e in range(E):
        Node_s, Node_e = map(int, input().split())
        if Node_e not in stack:
            stack.append(Node_e)
    print(stack)
