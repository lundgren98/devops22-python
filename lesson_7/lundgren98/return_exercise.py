def int_ret():
    return 1

def tuple_ret(x,y):
    return (x,y) 

def bool_ret():
    return True

def float_ret():
    return 1.3

def fullname(firstname, lastname):
    return f'{firstname} {lastname}'

def rectangle_area(h,w):
    return h * w

def sum_list(l):
    return sum(l)

def repeat_word(word, repeat=1):
    for i in range(repeat):
        print(word, end='')
    print()
