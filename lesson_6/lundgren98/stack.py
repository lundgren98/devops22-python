alphabet = 'abcdefghijklmnopqrstuvxyz'
letters = [x for x in alphabet]
stack = []
for l in letters:
    stack.append(l)

while len(stack) > 0:
    print(stack.pop(), end='')
print()
