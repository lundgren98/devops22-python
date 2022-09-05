

start = int(input('start: '))
stop = int(input('stop: '))
summation = 0
for i in range(start, stop):
    summation += i
    print(i)
print(f'sum: {summation}')
