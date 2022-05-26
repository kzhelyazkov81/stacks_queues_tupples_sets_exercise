first_set = set([int(x) for x in input().split(' ')])
second_set = set([int(x) for x in input().split(' ')])
n = int(input())

for _ in range(n):
    command_parts = input().split(' ')
    command = command_parts[0]
    target_set = command_parts[1]
    if command == 'Add':
        if target_set == "First":
            first_set = first_set.union([int(x) for x in command_parts[2:]])
        elif target_set == 'Second':
            second_set = second_set.union([int(x) for x in command_parts[2:]])
    elif command == 'Remove':
        if target_set == "First":
            first_set = first_set.difference([int(x) for x in command_parts[2:]])
        elif target_set == 'Second':
            second_set = second_set.difference([int(x) for x in command_parts[2:]])
    elif command == 'Check':
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print('True')
        else:
            print('False')

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
