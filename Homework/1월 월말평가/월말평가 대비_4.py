lst = [[1], [2 , 3], [4 , 5 , 6], [7 , 8 , 9 , 10]]

def all_list_sum(lst):
    result = 0
    for sub_lst in lst:
        for num in sub_lst:
            result += num
    return result
        

print(all_list_sum(lst))