def create_board(num):
    board = []
    for _ in range(num):
        current_row = input().split()
        board.append(current_row)
    return board


def get_position_by_direction(direction_string, x, y):
    if direction_string == "up":
        x -= 1
    elif direction_string == "down":
        x += 1
    elif direction_string == "left":
        y -= 1
    elif direction_string == "right":
        y += 1
    return x, y


size = 6

matrix = create_board(size)

start_row, start_col = eval(input())

data = input().split(", ")


while True:
    if data[0] == "Stop":
        break
    if data[0] == "Create":
        create_direction = data[1]
        value = data[2]
        row, col = get_position_by_direction(create_direction, start_row, start_col)
        if matrix[row][col] == ".":
            matrix[row][col] = value
        start_row, start_col = row, col

    elif data[0] == "Update":
        update_direction = data[1]
        value = data[2]
        row, col = get_position_by_direction(update_direction, start_row, start_col)
        if matrix[row][col] != ".":
            matrix[row][col] = value
        start_row, start_col = row, col

    elif data[0] == "Delete":
        del_direction = data[1]
        row, col = get_position_by_direction(del_direction, start_row, start_col)
        if matrix[row][col] != ".":
            matrix[row][col] = "."
        start_row, start_col = row, col

    elif data[0] == "Read":
        read_direction = data[1]
        row, col = get_position_by_direction(read_direction, start_row, start_col)
        if matrix[row][col] != ".":
            print(matrix[row][col])
        start_row, start_col = row, col

    data = input().split(", ")

for i in matrix:
    print(" ".join(i))
