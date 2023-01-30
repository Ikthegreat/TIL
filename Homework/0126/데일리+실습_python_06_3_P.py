# def count_vowels(word):
#     word_list = list(word)
#     count = 0
#     for i in word_list:
#         if i == 'a':
#             count += 1
#         elif i == 'e':
#             count += 1
#         elif i == 'i':
#             count += 1
#         elif i == 'o':
#             count += 1
#         elif i == 'u':
#             count += 1
#         else:
#             continue
#     return count

def count_vowels(word):
    word_list = list(word)
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in word:
        if i in vowels:
            count += 1
        else:
            continue
    return count


print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3