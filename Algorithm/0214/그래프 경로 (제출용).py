import sys
sys.stdin = open('그래프경로_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    V, E = map(int, input().split())
    Node = [[] for _ in range(V+1)]
    for e in range(E):
        Start, End = map(int, input().split())
        Node[Start].append(End)
        Node[End].append(Start)
    print(Node)
    S, G = map(int, input().split())
    stack = []
    for i in range(1, len(Node)):
        if G in Node[i]:
            stack.append(i)
            for j in range(len(Node[i])):
                stack.append(Node[i][j])
    print(stack)
    for s in stack:
        for i in range(1, len(Node)):
            if s in Node[i]:
                stack.append(i)
                for j in range(len(Node[i])):
                    stack.append(Node[i][j])
    print(stack)
