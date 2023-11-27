from collections import deque

monster_armor = deque(map(int, input().split(',')))
soldier_damage = list(map(int, input().split(',')))

defeated_monsters = 0

while monster_armor and soldier_damage:
    armor = monster_armor.popleft()
    damage = soldier_damage.pop()
    if damage >= armor:
        damage -= armor
        defeated_monsters += 1
        if len(soldier_damage) > 0:
            soldier_damage[-1] += damage
        elif len(soldier_damage) == 0 and damage > 0:
            soldier_damage.append(damage)

    elif damage < armor:
        monster_armor.append(armor - damage)

if not monster_armor:
    print("All monsters have been killed!")
if not soldier_damage:
    print("The soldier has been defeated.")

print(f'Total monsters killed: {defeated_monsters}')
