import random

a = list(range(1,101))
b = list(range(2,61,2))
c = list(range(1,78,2))
print(a)
print(b)
print(c)
d = random.choices(range(1,301), k=100)
print(d)

colors = ['blue', 'green', 'yellow', 'magenta', 'cyan']
new_colors = ['red']
new_colors.extend(random.choices(colors, k=2))
three_colors = random.choices(new_colors, k=50)
for l in (colors, new_colors, three_colors):
    print(f'{len(l)} {set(l)}')
