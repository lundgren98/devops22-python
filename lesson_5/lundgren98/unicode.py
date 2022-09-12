
cost = input('Your new car cost: ')
cost = '\u20bf ' + cost
if int(cost[2:]) < 50000:
    print('\N{grinning face}')
else:
    print('\N{grimacing face}')
