for i in range(10):

    N = int(input())
    Box_level = list(map(int, input().split()))

    sorted_level = sorted(Box_level)

    for j in range(N):
        sorted_level[-1] -= 1
        sorted_level[0] += 1
        sorted_level = sorted(sorted_level)

    flatten_level = sorted_level[-1] - sorted_level[0]

    print(f'#{i+1} {flatten_level}')
        

