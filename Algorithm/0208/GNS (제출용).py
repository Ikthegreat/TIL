import sys
sys.stdin = open('input_GNS.txt', 'r')

Test_case = int(input())
for t in range(Test_case):
    dummy, N = list(map(str, input().split()))
    N = int(N)
    string = list(map(str, input().split(' ')))
    sample = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    count = [0] * 10
    for i in range(10):
        for j in string:
            if j == sample[i]:
                count[i] += 1

    sorted_string = []
    for a in range(10):
        for b in range(count[a]):
            sorted_string.append(sample[a])

    result = ' '.join(list(map(str, sorted_string)))

    print(dummy)
    print(result)