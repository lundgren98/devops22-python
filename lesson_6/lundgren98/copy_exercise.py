from copy import copy, deepcopy

a = 'Hello, World!'
b = a
c = copy(a)
b += ' NOT!'
for i in (a,b,c):
    print(i)
