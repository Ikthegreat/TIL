import math

class Carsharing:
    
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance

    def rental(self):
        rental_fee = self.time * 120
        return rental_fee

    def insurance(self):
        insurance_fee = math.ceil(self.time / 30) * 525
        return insurance_fee

    def distence_fee(self):
        if self.distance > 100:
            km_fee = (170 * 100) + ((self.distance - 100) * 85)
        else:
            km_fee = 170 * self.distance
        return km_fee

    def fee(self):
        print(self.rental() + self.insurance() + self.distence_fee())

    # def fee(self, time, distance):
    #     total_fee = car_sharing.rental() + car_sharing.insurance() + car_sharing.distence_fee()
    #     return total_fee

car1 = Carsharing(600, 50)
car2 = Carsharing(600, 110)

car1.fee()
car2.fee()

# fee(600, 50) #=> 91000
# fee(600, 110) #=> 10
