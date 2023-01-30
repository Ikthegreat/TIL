grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

def expensive_grain(grain_lst):
    reversed_grain_lst = []
    for i in grain_lst:
        reversed_grain_lst.append(i[::-1])
    grain_cost_dict = dict(reversed_grain_lst)
    most_expensive = grain_cost_dict[max(grain_cost_dict.keys())]

    return most_expensive

print(expensive_grain(grain_lst))