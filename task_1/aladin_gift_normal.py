from collections import deque


materials = deque(map(int, input().split()))
magic_level = deque(map(int, input().split()))

diamond = 0
gem = 0
porcelain = 0
gold = 0

result = 0

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()
    result = material + magic

    if result < 100:
        if result % 2 == 0:
            result = material * 2 + magic * 3
        else:
            result = material * 2 + magic * 2
    elif result > 499:
        result = material / 2 + magic / 2

    if 100 <= result <= 199:
        gem += 1
    elif 200 <= result <= 299:
        porcelain += 1
    elif 300 <= result <= 399:
        gold += 1
    elif 400 <= result <= 499:
        diamond += 1

if (gem > 0 and porcelain > 0) or (gold > 0 and diamond > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")

if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

if diamond:
    print(f"Diamond Jewellery: {diamond}")
if gem:
    print(f"Gemstone: {gem}")
if gold:
    print(f"Gold: {gold}")
if porcelain:
    print(f"Porcelain Sculpture: {porcelain}")


