nums = input().split(' ')
first_integer = int(nums[0])
second_integer = int(nums[1])

moves = 0
opponents = 3
board = []

for i in range(first_integer):
    board.append(input().split(' '))


command = input()
while True:
    if command == 'Finish':
        break

    if opponents == 0:
        break

    start_row = None
    start_col = None
    for i in range(first_integer):
        for j in range(second_integer):
            if board[i][j] == 'B':
                start_row = i
                start_col = j
                break

    if command == 'up':
        row = start_row - 1
        col = start_col
        if row < 0 or row == first_integer:
            pass
        elif board[row][col] == 'P':
            opponents -= 1
            board[start_row][start_col] = '-'
            board[row][col] = 'B'
            moves += 1
            start_row = row
            start_col = col
        elif board[row][col] == '-':
            moves += 1
            board[start_row][start_col] = '-'
            board[row][col] = 'B'
    elif command == 'down':
        row = start_row + 1
        col = start_col
        if row < 0 or row == first_integer:
            pass
        elif board[row][col] == 'P':
            opponents -= 1
            board[start_row][start_col] = '-'
            board[row][col] = 'B'
            moves += 1
            start_row = row
            start_col = col
        elif board[row][col] == '-':
            moves += 1
            board[start_row][start_col] = '-'
            board[row][col] = 'B'
    elif command == 'left':
        row = start_row
        col = start_col - 1
        if col < 0 or col == second_integer:
            pass
        if board[row][col] == 'P':
            opponents -= 1
            board[start_row][start_col] = '-'
            board[row][col] = 'B'
            moves += 1
            start_row = row
            start_col = col
        elif board[row][col] == '-':
            moves += 1
            board[start_row][start_col] = '-'
            board[row][col] = 'B'
    elif command == 'right':
        row = start_row
        col = start_col + 1
        if col < 0 or col == second_integer:
            pass
        elif board[row][col] == 'P':
            opponents -= 1
            board[start_row][start_col] = '-'
            board[row][col] = 'B'
            moves += 1
            start_row = row
            start_col = col
        elif board[row][col] == '-':
            moves += 1
            board[start_row][start_col] = '-'
            board[row][col] = 'B'

    command = input()

print("Game over!")
print(f"Touched opponents: {3 - opponents} Moves made: {moves}")
