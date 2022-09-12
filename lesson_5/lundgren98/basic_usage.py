firstname = 'john'
lastname = 'smith'
tele = '00468123456789'

# 1
print(f'{firstname} {lastname} {tele}')
# 2-3
fullname = firstname + ' ' + lastname
# 4
for name in (fullname, firstname, lastname):
    print(len(name))
# 5
print(fullname + '\n' + tele)
# 6
print(fullname + ' ' + tele)
print(f'{fullname} {tele}')
print('{} {}'.format(fullname, tele))
print('%s %s' % (fullname, tele))
