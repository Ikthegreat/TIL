class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def tuple(self):
    #     return (self.x, self.y)

class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def get_area(self):
        return (self.point1.y - self.point2.y) * (self.point2.x - self.point1.x)

    def get_perimeter(self):
        return 2 * ((self.point1.y - self.point2.y) + (self.point2.x - self.point1.x))

    def is_square(self):
        if (self.point1.y - self.point2.y) == (self.point2.x - self.point1.x):
            return True
        else:
            return False
        

# 입력 예시
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)

print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

# 출력 예시
# 4
# 8
# True

# 9
# 12
# True