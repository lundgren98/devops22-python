def print_numbers(start=1, stop=11):
    for i in range(start, stop):
        print(i)

def print_string(s, reverse=False):
    if reverse:
        s = s[::-1]
    print(s)

print_string('hello world!')
print_string('hello world!', reverse=True)
