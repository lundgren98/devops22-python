def do_nothing():
    pass

def hello_world():
    print('hello world')

def one_equal():
    print(1 == 1.0)

def reverse_alphabet():
    alphabet = 'abcdefghijklmnopqrstuvxyz'
    print(alphabet[-1])

def hello_name(name):
    print(f'hello {name}')

def capital(word):
    print(word.upper())

def print_up_to(stop):
    for i in range(stop+1):
        print i
