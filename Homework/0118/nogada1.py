# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ]

word_list = ['eat','tea','tan','ate','nat','bat']

alphabet = {'a' : 1, 'b' : 2, 'e' : 3, 'n' : 4, 't' : 5}

reverse_alphabet = {1 : 'a', 2 : 'b', 3 : 'e', 4 : 'n', 5 : 't',}

lst = []

for i in range(0, 6):
    lst.append((alphabet[word_list[i][0]], alphabet[word_list[i][1]], alphabet[word_list[i][2]]))

print(lst)

s_lst = []

for i in range(0, 6):
     s_lst.append(tuple(sorted(lst[i])))

keyword = set(s_lst)

s0_lst = tuple(sorted(lst[0]))
s1_lst = tuple(sorted(lst[1]))
s2_lst = tuple(sorted(lst[2]))
s3_lst = tuple(sorted(lst[3]))
s4_lst = tuple(sorted(lst[4]))
s5_lst = tuple(sorted(lst[5]))

same0 = []
same1 = []
same2 = []

anagram0 = []
anagram1 = []
anagram2 = []

list_keyword = list(keyword)

if list_keyword[0] == s0_lst:
    same0.append(s0_lst)
    anagram0.append(0)

if list_keyword[0] == s1_lst:
    same0.append(s1_lst)
    anagram0.append(1)

if list_keyword[0] == s2_lst:
    same0.append(s2_lst)
    anagram0.append(2)

if list_keyword[0] == s3_lst:
    same0.append(s3_lst)
    anagram0.append(3)

if list_keyword[0] == s4_lst:
    same0.append(s4_lst)
    anagram0.append(4)

if list_keyword[0] == s5_lst:
    same0.append(s5_lst)
    anagram0.append(5)



if list_keyword[1] == s0_lst:
    same1.append(s0_lst)
    anagram1.append(0)

if list_keyword[1] == s1_lst:
    same1.append(s1_lst)
    anagram1.append(1)

if list_keyword[1] == s2_lst:
    same1.append(s2_lst)
    anagram1.append(2)

if list_keyword[1] == s3_lst:
    same1.append(s3_lst)
    anagram1.append(3)

if list_keyword[1] == s4_lst:
    same1.append(s4_lst)
    anagram1.append(4)

if list_keyword[1] == s5_lst:
    same1.append(s5_lst)
    anagram1.append(5)


if list_keyword[2] == s0_lst:
    same2.append(s0_lst)
    anagram2.append(0)

if list_keyword[2] == s1_lst:
    same2.append(s1_lst)
    anagram2.append(1)

if list_keyword[2] == s2_lst:
    same2.append(s2_lst)
    anagram2.append(2)

if list_keyword[2] == s3_lst:
    same2.append(s3_lst)
    anagram2.append(3)

if list_keyword[2] == s4_lst:
    same2.append(s4_lst)
    anagram2.append(4)

if list_keyword[2] == s5_lst:
    same2.append(s5_lst)
    anagram2.append(5)

print(anagram0)
print(anagram1)
print(anagram2)

anagram_set0 = []
anagram_set0.append(lst[anagram0[0]])
anagram_set0.append(lst[anagram0[1]])

anagram_set1 = []
anagram_set1.append(lst[anagram1[0]])

anagram_set2 = []
anagram_set2.append(lst[anagram2[0]])
anagram_set2.append(lst[anagram2[1]])
anagram_set2.append(lst[anagram2[2]])

print(anagram_set0)
print(anagram_set1)
print(anagram_set2)

final1 = []
final2 = []
final3 = []

final1 = [reverse_alphabet[anagram_set0[0][0]],reverse_alphabet[anagram_set0[0][1]],reverse_alphabet[anagram_set0[0][2]]], [reverse_alphabet[anagram_set0[1][0]], reverse_alphabet[anagram_set0[1][1]], reverse_alphabet[anagram_set0[1][2]]]
final2 = [reverse_alphabet[anagram_set1[0][0]],reverse_alphabet[anagram_set1[0][1]],reverse_alphabet[anagram_set1[0][2]]]
final3 = [reverse_alphabet[anagram_set2[0][0]],reverse_alphabet[anagram_set2[0][1]],reverse_alphabet[anagram_set2[0][2]]], [reverse_alphabet[anagram_set2[1][0]], reverse_alphabet[anagram_set2[1][1]], reverse_alphabet[anagram_set2[1][2]]], [reverse_alphabet[anagram_set2[2][0]], reverse_alphabet[anagram_set2[2][1]], reverse_alphabet[anagram_set2[2][2]]]

real_final = [final1, final2, final3]

print(final1)
print(final2)
print(final3)

str1 = ''.join(s for s in final1[0])
str2 = ''.join(s for s in final1[1])

str3 = final2.split()

str4 = ''.join(s for s in final3[0])
str5 = ''.join(s for s in final3[1])
str6 = ''.join(s for s in final3[2])

print([str1, str2], [str3], [str4, str5, str6])



