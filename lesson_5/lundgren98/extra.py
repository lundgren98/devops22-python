current_salary = 40000
currency = '\u20bf'
print(f'Your current salary is {currency} {current_salary}')
offer_num = 0
accept = False
while not accept or offer_num <= 1:
    if offer_num > 0:
        print('NO')
    increase = int(input(f'How much more do you want? {currency} '))
    print('\N{grinning face}')
    accept = (increase / current_salary) < 0.05
    offer_num += 1
print('YES')
    
