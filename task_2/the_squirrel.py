def squirrel_next_position(x, y, direction):
    if direction == "up":
        x -= 1
    elif direction == "down":
        x += 1
    elif direction == "left":
        y -= 1
    elif direction == "right":
        y += 1
    return x, y


def get_squirrel_stats(command_list, matrix, matrix_row, matrix_col):
    hazelnuts = 0

    for command in command_list:
        row, col = squirrel_next_position(matrix_row, matrix_col, command)

        if row < 0 or row == num or col < 0 or col == num:
            result = f"The squirrel is out of the field.\n" + f"Hazelnuts collected: {hazelnuts}"
            return result

        if matrix[row][col] == 't':
            result = "Unfortunately, the squirrel stepped on a trap...\n" + f"Hazelnuts collected: {hazelnuts}"
            return result

        elif matrix[row][col] == '*':
            matrix[row][col] = 's'
            matrix[matrix_row][matrix_col] = '*'
            matrix_row, matrix_col = row, col

        elif matrix[row][col] == 'h':
            hazelnuts += 1
            matrix[row][col] = 's'
            matrix[matrix_row][matrix_col] = '*'
            matrix_row, matrix_col = row, col

    if hazelnuts < 3:
        result = "There are more hazelnuts to collect.\n" + f"Hazelnuts collected: {hazelnuts}"
        return result
    else:
        result = "Good job! You have collected all hazelnuts!\n" + f"Hazelnuts collected: {hazelnuts}"
        return result


num = int(input())

commands = input().split(', ')

board = []
start_row = None
start_col = None

for i in range(num):
    row_data = input()
    current_row = []
    for j in range(len(row_data)):
        current_row.append(row_data[j])
        if row_data[j] == 's':
            start_row = i
            start_col = j
    board.append(current_row)

print(get_squirrel_stats(commands, board, start_row, start_col))
