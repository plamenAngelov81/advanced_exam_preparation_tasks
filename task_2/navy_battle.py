def submarine_next_position(x, y, direction):
    if direction == "up":
        x -= 1
    elif direction == "down":
        x += 1
    elif direction == "left":
        y -= 1
    elif direction == "right":
        y += 1
    return x, y


def get_start_coordinates(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if matrix[i][j] == "S":
                return i, j


def last_know_position(some_board):
    result = ''
    for k in some_board:
        result += f"{(''.join(x for x in k))}\n"
    return result


size = int(input())
destroyed_ships = 0
mines_hit = 3
matrix = []

for _ in range(size):
    row = [x for x in input()]
    matrix.append(row)


start_row, start_col = get_start_coordinates(matrix)

command = input()

while True:

    current_row, current_col = submarine_next_position(start_row, start_col, command)
    matrix[start_row][start_col] = "-"

    if matrix[current_row][current_col] == '-':
        matrix[current_row][current_col] = 'S'
        start_row, start_col = current_row, current_col

    elif matrix[current_row][current_col] == "C":
        destroyed_ships += 1
        matrix[current_row][current_col] = 'S'

    elif matrix[current_row][current_col] == "*":
        mines_hit -= 1
        matrix[current_row][current_col] = 'S'

    start_row, start_col = current_row, current_col

    if destroyed_ships == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

    if mines_hit == 0:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{start_row}, {start_col}]!")
        break

    command = input()

print(last_know_position(matrix))
