from collections import Counter

entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

def most_visited():
    print("입장 기록 많은 Top3")
    entrylist = Counter(entry_record)
    reverse_entrylist = dict(map(reversed, entrylist.items()))

    top3 = sorted(reverse_entrylist)[-3:]
    for i in range(-1, -4, -1):
        print(f'{reverse_entrylist[top3[i]]} {top3[i]}회')

def visit_count_difference():
    print("출입 기록이 수상한 사람")
    entry_count = Counter(entry_record)
    exit_count = Counter(exit_record)
    difference_list = []
    for i in entry_count.keys():
        difference = entry_count[i] - exit_count[i]
        difference_list.append(difference)
    
    same_list = []
    exit_many = []
    entry_many = []
    difference_dict = dict(zip(entry_count.keys(), difference_list))
    for key, value in difference_dict.items():
        if value == 0:
            same_list.append(key)
        elif value < 0:
            exit_many.append(key)
        else:
            entry_many.append(key)

    for a in entry_many:
        print(f'{a}은 입장 기록이 {abs(difference_dict[a])}회 더 많아 수상합니다.')

    for c in exit_many:
        print(f'{c}은 퇴장 기록이 {abs(difference_dict[c])}회 더 많아 수상합니다.')
            

most_visited()
print(' ')
visit_count_difference()