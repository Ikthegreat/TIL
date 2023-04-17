import sys
sys.stdin = open('spin_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N, M = map(int, input().split())
    num_arr = list(map(int, input().split()))
    for spin in range(M):
        num_arr.append(num_arr.pop(0))
    print(f'#{t+1} {num_arr[0]}')