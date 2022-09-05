
def q1():
    for i in range(10):
        print('hello!')

def q2():
    for i in range(1, 10):
        print(str(i) * i)

def q3():
    number = 348
    while True:
        guess = int(input('Enter an integer : '))
        if (guess < number):
            print('Wrong, it\'s higher')
            continue
        if (guess > number):
            print('Wrong, it\'s lower.')
            continue
        print('Congratulations, you\'re correct!')
        break

def q4():
    numbers = [2, 4, 42, 360, 1080, 69, 720, 420]
    for n in numbers:
        if n % 2:
            print('Not allowed!')
            break
        print(n)

def q5():
    first_list = [3, 7, 9, 2, 6]
    second_list = [2, 3, 6, 7, 9]
    list_indeces = []
    for n in second_list:
        list_indeces.append((n,first_list.index(n)))
    print(list_indeces)

def q7():
    fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
    l = len(fruits)
    space = int(input('How much space do you have in your basket? '))
    my_basket = []
    for i in range(space):
        my_basket.append(fruits[i%l])
    print(my_basket)

def q8():
    primes = []
    p = 2
    while p < 100:
        n = 2 
        while p%n != 0:
            n += 1
        if (n == p):
            primes.append(p)
        p += 1
    print(primes)




if __name__ == '__main__':
    #q1()
    #q2()
    #q3()
    #q4()
    #q5()
    #q7()
    q8()
