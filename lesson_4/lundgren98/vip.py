
names = ('adam', 'bertil', 'caesar', 'david', 'erik')
name = input('What\'s your name? ').lower()
if (name in names):
    print(f'Welcome {name.title()}')
else:
    print('Sorry, you are not on the list')
