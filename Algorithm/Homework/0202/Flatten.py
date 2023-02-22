def counting_sort(input_list):
    max_num = 0
    for m in input_list:
        if m > max_num:
            max_num = m

    sorted_list = [0] * len(input_list)
    count_list = [0] * (max_num+1)

    for a in input_list:
        count_list[a] += 1

    for b in range(1, max_num+1):
        count_list[b] += count_list[b-1]

    for c in input_list:
        idx = count_list[c]
        sorted_list[idx - 1] = c
        count_list[c] -= 1

    return sorted_list

for t in range(10):

    N = int(input())
    Box_level = list(map(int, input().split()))

    sorted_level = counting_sort(Box_level)

    for j in range(N):
        sorted_level[-1] -= 1
        sorted_level[0] += 1
        sorted_level = counting_sort(sorted_level)
        if sorted_level[-1] - sorted_level[0] <= 1:
            break

    flatten_level = sorted_level[-1] - sorted_level[0]

    print(f'#{t+1} {flatten_level}')