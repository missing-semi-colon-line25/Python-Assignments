class Quad:
    def __init__(self, s1, s2, s3, s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4


class Square(Quad):
    def __init__(self, s1):
        super(Square, self).__init__(s1, s1, s1, s1)

    def area(self):
        return self.s1 ** 2


class Rectangle(Quad):
    def __init__(self, s1, s2):
        super(Rectangle, self).__init__(s1, s2, s1, s2)

    def area(self):
        return self.s1 * self.s2 * 2


sq_side = int(input("Enter square side"))
sq1 = Square(sq_side)
rs1, rs2 = input("enter rectangle sides , separated by ','").split(',')

rec1 = Rectangle(int(rs1), int(rs2))

print(f"Perimeter of square: {sq1.perimeter()}, Area of square: {sq1.area()}")
print(f"Perimeter of rectangle: {rec1.perimeter()}, Area of rectangle: {rec1.area()}")
