from collections import namedtuple
from math import sqrt

Point = namedtuple('Point', ['x', 'y'])

a = Point(x=2, y=3)
b = Point(x=5, y=7)

board = [['-']*10 for i in range (10)]

board[a.y][a.x] = '*'
board[b.y][b.x] = '*'

for row in board:
    print(row)

distance = sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
print(f'The distance between {a} and {b} is {distance}')


