Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    card = list(map(int, input()))

    card_list = [0] * 10
    count = 0
    max_card = 0

    for i in card:
        card_list[i] += 1

    for j in range(len(card_list)):
        if count <= card_list[j]:
            count = card_list[j]
            max_card = j
        else:
            continue

    print(f'#{t+1} {max_card} {count}')