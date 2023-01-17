orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

lst_orders = list(orders.split(','))

ice_drinks = 0
for i in lst_orders:
    if '아이스' in i:
        ice_drinks += 1
    else:
        continue

print(f'아이스 음료는 총 {ice_drinks}잔 입니다.')

iceamericano = 0
icecaramel = 0
icelatte = 0
americano = 0
lattemacciato = 0
espresso = 0
caramel = 0
capuccino = 0
hotchoco = 0

for i in lst_orders:
    if i == '아이스아메리카노':
        iceamericano += 1
    elif i == '아이스카라멜마키야또':
        icecaramel += 1
    elif i == '아이스라떼':
        icelatte += 1
    elif i == '아메리카노':
        americano += 1
    elif i == '라떼마키야또':
        lattemacciato += 1
    elif i == '에스프레소':
        espresso += 1
    elif i == '카라멜마키야또':
        caramel += 1
    elif i == '카푸치노':
        capuccino += 1
    elif i == '핫초코':
        hotchoco += 1

drink_count = {'아이스아메리카노' : iceamericano, '아이스카라멜마키야또' : icecaramel, '아이스라떼' : icelatte, '아메리카노' : americano,
'라떼마키야또' : lattemacciato, '에스프레소' : espresso, '카라멜마키야또' : caramel, '카푸치노' : capuccino, '핫초코' : hotchoco}

print(drink_count)