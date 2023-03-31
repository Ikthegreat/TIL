import sys
sys.stdin = open('정식.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    bi = list(input())
    tri = list(input())
    temp_bi = []
    temp_tri = []
    for i in range(len(bi)):
        temp = bi[:]
        if temp[i] == '0':
            temp[i] = '1'
        elif temp[i] == '1':
            temp[i] = '0'
        temp_bi.append(te
