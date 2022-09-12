from collections import Counter
import random

names = ['adam', 'bertil', 'caesar', 'david', 'erik', 'folke', 'gustaf',
        'harald', 'isak', 'jakob', 'karl']
people = random.choices(names, k=100)
c = Counter(people)
print('Top 3 common names')
for name, count in c.most_common()[:3]:
    print(name)
print('Least common name')
print(c.most_common()[-1][0])
unique_names = list(set(people))
print(sorted(unique_names))
random.shuffle(unique_names)
print(unique_names)
print(sorted(unique_names, reverse=True))
