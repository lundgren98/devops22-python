class Circle:
    def __init__(self, diag, color='grey'):
        self.diag = diag
        self.color = color
        self.area = self.__area()
        self.circumference = self.__circumference()

    def __area(self):
        from math import pi
        return float(pi * self.diag * self.diag / 4)

    def __circumference(self):
        from math import pi
        return float(pi * self.diag / 2)

    def set_color(color):
        self.color = color

if __name__ == '__main__':
    my_circle = Circle(2)
    print(my_circle.color)
