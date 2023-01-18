import calendar

year = int(input('연도를 입력하세요 : '))

leapcheck = calendar.isleap(year)

while leapcheck:
    print('윤년입니다. 연도를 다시 입력해주세요.')
    year = int(input('연도를 입력하세요 : '))
    leapcheck = calendar.isleap(year)
    if leapcheck == False:
        print(calendar.calendar(year))
        break

if leapcheck == False:
    print(calendar.calendar(year))

year = int(input('연도를 입력하세요 : '))
month = int(input('월을 입력하세요 : '))
day = int(input('일을 입력하세요 : '))

day_of_the_week = calendar.weekday(year, month, day)

if day_of_the_week == 0:
    print('경고 월요일입니다.')

day_count = {0 : '월요일', 1 : '화요일', 2 : '수요일', 3 : '목요일', 4 : '금요일', 5 : '토요일', 6 : '일요일'}

print({'년': year, '월': month,'일': day,'요일': day_count[day_of_the_week]})