class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return float(self.side ** 2)

    def circumference(self):
        return float(self.side * 4)

if __name__ == '__main__':
    first_square = Square(2)
    second_square = Square(3.5)
    for square in (first_square, second_square):
        print(f'area: {square.area()}')
        print(f'circumference: {square.circumference()}')
