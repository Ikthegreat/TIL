def counting_sort(input_list):
    max_num = 0
    for m in input_list:
        if m > max_num:
            max_num = m

    sorted_list = [0] * len(input_list)
    count_list = [0] * (max_num+1)

    for i in input_list:
        count_list[i] += 1

    for j in range(1, max_num+1):
        count_list[j] += count_list[j-1]

    for k in input_list:
        idx = count_list[k]
        sorted_list[idx - 1] = k
        count_list[k] -= 1

    return sorted_list