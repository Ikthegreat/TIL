import sys
sys.stdin = open('간단한압축풀기_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    temp = []
    nums = []
    sum_nums = 0
    for n in range(N):
        C, K = map(str, input().split())
        K = int(K)
        nums.append(K)
        for i in range(K):
            temp.append(C)
    for a in range(len(nums)):
        sum_nums += nums[a]
    if sum_nums % 10 == 0:
        line = sum_nums // 10
    else:
        line = sum_nums // 10 + 1
    document = [[0] * 10 for i in range(line)]
    for j in range(len(temp)):
        document[j // 10][j % 10] = temp[j]
    print(f'#{t+1}')
    for x in range(line):
        for y in range(10):
            if document[x][y] == 0:
                document[x] = document[x][:y]
                break
        result = ''.join(list(map(str, document[x])))

        print(result)
