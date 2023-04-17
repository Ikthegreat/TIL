import sys
sys.stdin = open('16to10.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    hexadecimal = list(input())
    hexa_dict = {'A': 10, 'B': 11}
    for h in range(len(hexadecimal)):


binary = list(map(int, input()))
binary = binary[::-1]
result = []
for i in range(0, len(binary), 7):
    num = 0
    for j in range(i, i + 7):
        num += binary[j] * (2 ** (j % 7))
    result.append(num)