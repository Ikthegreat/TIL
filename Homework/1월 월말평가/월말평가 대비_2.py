# def list_sum(*args):
#     num = 0
#     for i in range(0, len(args)):
#         num = num + list(args)[i]
#     return num

# print(list_sum([1, 2, 3, 4]))

lst = [1, 2, 3, 4, 5]

def list_sum(lst):
    result = 0
    for num in lst:
        result = result + num
    return result

print(list_sum(lst))

