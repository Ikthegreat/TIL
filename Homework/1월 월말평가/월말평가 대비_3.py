lst = [
    {'name' : 'kim', 'age' : 12},
    {'name' : 'lee', 'age' : 4}
    ]

def dict_list_sum(lst):
    result = 0
    for dic in lst:
        result += dic['age']
    return result

print(dict_list_sum(lst))