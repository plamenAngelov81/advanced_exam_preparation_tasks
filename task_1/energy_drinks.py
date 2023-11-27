from collections import deque

# take last caffeine
caffeine = list(map(int, input().split(', ')))
# and first drink
energy_drinks = deque(map(int, input().split(', ')))

max_caffeine = 300
sleep_caffeine = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_energy = energy_drinks.popleft()
    caffeine_result = current_caffeine * current_energy
    if caffeine_result + sleep_caffeine <= max_caffeine:
        sleep_caffeine += caffeine_result
    else:
        sleep_caffeine -= 30
        if sleep_caffeine < 0:
            sleep_caffeine = 0
        energy_drinks.append(current_energy)

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {sleep_caffeine} mg caffeine.")