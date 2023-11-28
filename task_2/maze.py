def possible_moves(x, y, matrix_row, matrix_col, board):
    possible_cells = [
        [x + 1, y],
        [x - 1, y],
        [x, y + 1],
        [x, y - 1]
    ]

    def is_inside(r, c):
        return 0 <= r < matrix_row and 0 <= c < matrix_col and board[r][c] != "#"

    turns = []
    for k in possible_cells:
        a, b = k
        if is_inside(a, b):
            turns.append([a, b])
    return turns


matrix = []

row = 4
col = 5

for i in range(row):
    add_row = [x for x in input()]
    matrix.append(add_row)

current_row = 0
current_col = 0
exit_condition = False
while True:
    if matrix[current_row][current_col] == "X":
        exit_condition = True
        break

