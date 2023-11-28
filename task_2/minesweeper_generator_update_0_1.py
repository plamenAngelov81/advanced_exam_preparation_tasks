import random


def possible_cells(r, c, num):
    cells = [
        [r - 1, c - 1],
        [r - 1, c],
        [r - 1, c + 1],
        [r, c - 1],
        [r, c + 1],
        [r + 1, c - 1],
        [r + 1, c],
        [r + 1, c + 1]
    ]
    surrounding_cells = []
    for x, y in cells:
        if 0 <= x < num and 0 <= y < num:
            surrounding_cells.append([x, y])
    return surrounding_cells


size = int(input())

mine = "*"
save = "-"

combination = mine + save

field = []

for i in range(size):
    current_row = random.choices(combination, weights=[15, 35], k=size)
    field.append(current_row)

for row in range(size):
    for col in range(size):
        if field[row][col] == "*":
            continue
        bomb_counter = 0
        for i in possible_cells(row, col, size):
            a, b = i
            if field[a][b] == "*":
                bomb_counter += 1

        field[row][col] = str(bomb_counter)
for k in field:
    print(*k, sep=" ")
