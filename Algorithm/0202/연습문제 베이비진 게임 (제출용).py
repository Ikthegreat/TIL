Test_case = int(input())

for t in range(Test_case):
    Card = list(map(int, input()))
    Card_count = [0] * 12
    for i in range(0, len(Card)):
        Card_count[Card[i]] += 1

    j = tri_case = run_case = 0

    while j < 10:
        if Card_count[j] >= 3:
            tri_case += 1
            Card_count[j] -= 3
            continue

        elif Card_count[j] >= 1 and Card_count[j+1] >= 1 and Card_count[j+2] >= 1:
            run_case += 1
            Card_count[j] -= 1
            Card_count[j+1] -= 1
            Card_count[j+2] -= 1
            continue

        else:
            j += 1

    if (tri_case + run_case) == 2:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')