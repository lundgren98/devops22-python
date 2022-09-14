
def odd_input():
    try:
        i = int(input('Type an integer: '))
        if i % 2 == 0:
            raise Exception('Even numbers is not allowed')
    except ValueError:
        print('Sorry, not an int')
        odd_input()

odd_input()
