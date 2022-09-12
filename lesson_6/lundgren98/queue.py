import random
from collections import deque

names = ['adam', 'bertil', 'caesar', 'david', 'erik', 'folke', 'gustaf',
        'harald', 'isak', 'jakob', 'karl']
before_queue = random.choices(names, k=50)
queue = [before_queue.pop() for i in range(10)]
queue = deque(queue)

while len(queue) > 0:
    print(queue)
    remove_from_queue = random.choice(range(1,len(queue) + 1))
    for i in range(remove_from_queue):
        queue.popleft()
    for i in range(remove_from_queue):
        if len(before_queue) < 1:
            break
        queue.append(before_queue.pop())


