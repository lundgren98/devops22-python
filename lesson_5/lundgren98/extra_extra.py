# 1
def q1():
    first_string = input('Type your first string: ')
    second_string = input('Type your second string: ')
    new_first_string = "'" + first_string + "'"
    new_second_string = '"' + second_string + '"'
    combined_string = new_first_string + '\n' + new_second_string
    print(combined_string)

# 2
def q2():
    a = int(input('Input a number: '))
    b = int(input('Input a second number: '))
    summation = "The sum of " + str(a) + " and " + str(b) + " is " + str(a + b)
    difference = "The difference of %d and %d is %d" % (a, b, a - b)
    product = "The product of {} and {} is {}".format(a, b, a * b)
    quotient = f"The quotient of {a} and {b} is {a/b}"
    print(summation)
    print(difference)
    print(product)
    print(quotient)

# 3
def q3():
    a = 'Jag tYcker om äGg'
    b = 'inte'
    c = 'SPAM'
    d = ' '

    print(a)
    words = a.split(d)
    words.insert(2, b)
    s = d.join(words)
    print(f"Lade in '{b}' -> {s}")
    s = s.title()
    print(f"Title -> {s}")
    s = s.swapcase()
    print(f"Swapcase -> {s}")
    words = s.split(d)
    s = s.replace(words[-1], c)
    print(f"Bytte ut '{words[-1]}' mot '{c}' -> {s}")

if __name__ == '__main__':
    q1()
    q2()
    q3()
