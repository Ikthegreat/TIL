import sys
sys.stdin = open('다솔이다이아몬드_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    string = input()
    N = 1 + 4 * len(string)
    diamond = [['.'] * N for _ in range(N)]

    for n in range(N):
        print(*diamond[n])