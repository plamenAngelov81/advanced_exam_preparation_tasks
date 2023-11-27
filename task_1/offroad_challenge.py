from collections import deque

fuel = list(map(int, input().split(' ')))
consumption_indexes = deque(map(int, input().split(' ')))
quantities = deque(map(int, input().split(' ')))

quantities_counter = 0
reached_altitudes = []

while fuel and consumption_indexes and quantities:

    current_fuel = fuel.pop()
    current_index = consumption_indexes.popleft()
    quantity = quantities.popleft()

    result = current_fuel - current_index

    if result >= quantity:
        print(f"John has reached: Altitude {quantities_counter + 1}")
        reached_altitudes.append(f'Altitude {quantities_counter + 1}')
    else:
        print(f'John did not reach: Altitude {quantities_counter + 1}')
        break
    quantities_counter += 1

if 0 < len(reached_altitudes) < 4:
    print('John failed to reach the top.')
    print(f'Reached altitudes: {", ".join(reached_altitudes)}')
elif len(reached_altitudes) == 0:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
elif len(reached_altitudes) == 4:
    print('John has reached all the altitudes and managed to reach the top!')
