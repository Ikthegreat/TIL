# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 

def de_identify(identify_number):
    list_id_num = list(identify_number)
    block_id_num = ''.join(list_id_num[0 : 6]) + '*******'

    return block_id_num

print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))