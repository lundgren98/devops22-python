
def valuecatch(t, s):
    while True:
        try:
            return t(input(s))
        except ValueError:
            print('Wrong Type!')

def inputing():
    s = input('Type a string: ')
    print(s)
    i = valuecatch(int, 'Type an integer: ')
    print(i * 2)
    s = input('Type a string: ')
    print(s + s)
    f = valuecatch(float, 'Type a float: ')
    print(f / 3.5)


if __name__ == "__main__":
    inputing()
