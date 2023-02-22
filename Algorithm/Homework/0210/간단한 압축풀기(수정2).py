import sys
sys.stdin = open('간단한압축풀기_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    string = ''
    sum_nums = 0
    for n in range(N):
        C, K = map(str, input().split())
        K = int(K)
        string += C * K
        sum_nums += K
    print(f'#{t + 1}')
    for i in range(sum_nums//10+30):
        print(string[i*10:i*10+10])
