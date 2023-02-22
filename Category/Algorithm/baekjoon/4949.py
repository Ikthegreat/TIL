string = input()

B_1 = 0  # [
B_2 = 0  # ]
S_1 = 0  # (
S_2 = 0  # )

for i in range(len(string)):
    if string[i] == '[':
        B_1 += 1
    elif string[i] == ']':
        B_2 += 1
    elif string[i] == '(':
        S_1 += 1
    elif string[i] == ')':
        S_2 += 1

if B_1 == B_2 and S_1 == S_2:
    print('yes')
else:
    print('no')
