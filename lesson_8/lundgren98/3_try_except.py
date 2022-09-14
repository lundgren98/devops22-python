
def divide(x, y):
    try:
        if isinstance(y, str):
            raise TypeError
        return x / y
    except ZeroDivisionError: 
        print('Division by zero is not allowed')


print(divide(2, "hello"))
