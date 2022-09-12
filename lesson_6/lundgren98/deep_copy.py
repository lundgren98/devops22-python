from copy import copy, deepcopy

names = ['adam', 'bertil', 'caesar']
a = names
b = copy(names)
c = deepcopy(names)
names.pop()
names.append('david')
for i in (a,b,c):
    print(i)
