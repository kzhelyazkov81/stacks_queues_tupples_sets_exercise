from collections import deque

materials = [int(x) for x in input().split(' ')]
magics = deque([int(x) for x in input().split(' ')])

crafting_table = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted_toys = {}

while materials and magics:
    material = materials.pop()
    magic = magics.popleft()
    if material == 0 and magic == 0:
        continue
    if material == 0:
        magics.appendleft(magic)
        continue
    if magic == 0:
        materials.append(material)
        continue

    result = material * magic

    if result in crafting_table:
        toy = crafting_table[result]
        if toy not in crafted_toys:
            crafted_toys[toy] = 0
        crafted_toys[toy] += 1
        continue

    if result < 0:
        material += magic
        materials.append(material)
    else:
        material += 15
        materials.append(material)

if ('Doll' in crafted_toys and 'Wooden train' in crafted_toys) or ('Teddy bear' in crafted_toys and 'Bicycle' in crafted_toys):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    material_left = ', '.join([str(x) for x in reversed(materials)])
    print(f'Materials left: {material_left}')
if magics:
    magic_left = ', '.join([str(x) for x in magics])
    print(f'Magic left: {magic_left}')

for toy, amount in sorted(crafted_toys.items()):
    print(f'{toy}: {amount}')
