import sys
sys.stdin = open('input_GNS.txt', 'r')

Test_case = int(input())
for t in range(Test_case):
    dummy, N = list(map(str, input().split()))
    N = int(N)
    string = list(map(str, input().split(' ')))
    sample = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    sorted_string = []

    for i in range(10):
        for j in string:
            if j == sample[i]:
                sorted_string.append(j)

    result = ' '.join(list(map(str, sorted_string)))

    print(f'#{t+1}')
    print(result)