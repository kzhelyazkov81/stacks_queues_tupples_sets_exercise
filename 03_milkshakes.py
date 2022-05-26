from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milk_cups = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while chocolates and milk_cups and milkshakes < 5:
    chocolate = chocolates.pop()
    milk_cup = milk_cups.popleft()

    if milk_cup <= 0 and chocolate <= 0:
        continue
    elif milk_cup <= 0:
        chocolates.append(chocolate)
        continue
    elif chocolate <= 0:
        milk_cups.appendleft(milk_cup)
        continue

    if chocolate == milk_cup:
        milkshakes += 1
    else:
        milk_cups.append(milk_cup)
        chocolates.append(chocolate - 5)


if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolates:
    chocolates_left = ', '.join(str(x) for x in chocolates)
    print(f'Chocolate: {chocolates_left}')
else:
    print('Chocolate: empty')

if milk_cups:
    milk_cups_left = ', '.join(str(x) for x in milk_cups)
    print(f'Milk: {milk_cups_left}')
else:
    print('Milk: empty')
