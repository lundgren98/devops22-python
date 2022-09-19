class Rectangle:
    def __init__(self, h: int = 1, w: int = 1):
        self.h = h
        self.w = w

    def show(self):
        tb = '+' + self.w*'-' + '+\n'
        m  = '|' + self.w*' ' + '|\n'
        s  = tb + self.h*m + tb 
        print(s)

    @classmethod
    def create_rectangle(cls):
        try:
            h = int(input('h: '))
            w = int(input('w: '))
            if h < 1 or w < 1:
                raise Exception
        except TypeError:
            print('not an int!')
            return cls.create_rectangle()
        except Exception:
            print('All sides must be positive')
            return cls.create_rectangle()
        return cls(h, w)

class Rectangles:
    def __init__(self):
        self._list = []

    def append(self):
        self._list.append(Rectangle.create_rectangle())

    def show(self):
        if len(self._list) < 1:
            print('No object available to print')
            return
        self._list[-1].show()

    def delete(self):
        if len(self._list) < 1:
            print('No object to delete')
            return
        self._list.pop()
