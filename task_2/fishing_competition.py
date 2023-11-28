def boat_position(x, y, command, board_size):
    if command == 'up':
        x -= 1
        if x < 0:
            x = board_size - 1
    elif command == 'down':
        x += 1
        if x == board_size:
            x = 0
    elif command == 'left':
        y -= 1
        if y < 0:
            y = board_size - 1
    elif command == 'right':
        y += 1
        if y == board_size:
            y = 0

    return x, y


size = int(input())

fishing_area = []
quota = 20
fish_tons = 0
start_row = None
start_col = None
whirlpool = False

for i in range(size):
    row = []
    current_row = input()
    for ch in range(len(current_row)):
        row.append(current_row[ch])
        if current_row[ch] == 'S':
            start_row = i
            start_col = ch
    fishing_area.append(row)

direction = input()

while True:
    if direction == 'collect the nets':
        break
    fishing_area[start_row][start_col] = '-'
    row, col = boat_position(start_row, start_col, direction, size)

    if fishing_area[row][col] == '-':
        pass
    elif fishing_area[row][col] == 'W':
        whirlpool = True
        fish_tons = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{row},{col}]")
        break
    else:
        fish_passage = int(fishing_area[row][col])
        fish_tons += fish_passage
        fishing_area[row][col] = 'S'

    fishing_area[row][col] = 'S'
    start_row, start_col = row, col

    direction = input()

if not whirlpool:
    if fish_tons >= 20:
        print('Success! You managed to reach the quota!')
    else:
        diff = quota - fish_tons
        print(f"You didn't catch enough fish and didn't reach the quota! You need {diff} tons of fish more.")

    if fish_tons > 0:
        print(f'Amount of fish caught: {fish_tons} tons.')

    for area in fishing_area:
        print(f'{"".join(area)}')
