orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

lst_orders = list(orders.split(',')) # ','를 기준으로 List 생성

set_lst_orders = set(lst_orders) # Set으로 List 내에서 중복 제거

ordered_menu = list(set(lst_orders)) # 다시 List로 변환

print(f'총 {len(lst_orders)}잔') # len으로 List 내에서 데이터 수량 확인

print(sorted(ordered_menu, reverse = True)) # sorted( , reverse = True)로 내림차순 정렬