

class A:
    def show(self):
        return 'AAAAAAA'

class B(A):
    def show(self):
        return 'BBBBBBB'

def main():
    a = A()
    b = B()
    print(a.show())
    print(b.show())

if __name__ == '__main__':
    main()
