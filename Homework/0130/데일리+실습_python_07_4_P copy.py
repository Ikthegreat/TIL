import math

def fee(time, distance):

    rental_fee = time * 120

    rental_time = math.ceil(time / 30) * 30
    insurance_fee =  rental_time / 30 * 525

    if distance > 100:
        distance_fee = (170 * 100) + ((distance - 100) * 85)
    else:
        distance_fee = 170 * distance

    total_fee = rental_fee + insurance_fee + distance_fee

    return int(total_fee)

print(fee(600, 50)) #=> 91000
print(fee(600, 110)) #=> 10
