from collections import deque

working_bees = deque([int(x) for x in input().split(' ')])
nectar = [int(x) for x in input().split(' ')]
symbols = deque([x for x in input().split(' ')])

operations = {
    '+': lambda a, b: a+b,
    '-': lambda a, b: a-b,
    '*': lambda a, b: a*b,
    '/': lambda a, b: a//b
}

total_honey = 0

while working_bees and nectar:
    first_bee = working_bees.popleft()
    last_nectar = nectar.pop()
    if last_nectar < first_bee:
        working_bees.appendleft(first_bee)
        continue
    operation = symbols.popleft()
    total_honey += abs(operations[operation](first_bee, last_nectar))

print(f'Total honey made: {total_honey}')
if working_bees:
    bees_left = ', '.join(str(x) for x in working_bees)
    print(f'Bees left: {bees_left}')
if nectar:
    nectar_left = ', '.join(str(x) for x in nectar)
    print(f'Nectar left: {nectar_left}')
