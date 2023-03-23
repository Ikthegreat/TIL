def insurance(time):
    count = 0
    while True:
        if time == 50:
            count += 1
            return count
        elif time > 50:
            time -= 30
            count += 1
        elif 30 < time < 50:
            return count + 1
        elif time > 30

print(insurance(40))

# time = 300

# time_list = []

# for i in range(1000):
#     if time == (30 * i):
#         time_list.append(i)
#     elif time 
#     else:
#         continue