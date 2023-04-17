for t in range(10):
    Test_case = int(input())
    char = input()
    string = input()
    count = 0
    for i in range(len(string) + 1 - len(char)):
        if char == string[i:(i + len(char))]:
            count += 1

    print(f'#{Test_case} {count}')