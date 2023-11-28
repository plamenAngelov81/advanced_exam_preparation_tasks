def mouse_next_position(x, y, direction):
    if direction == "up":
        x -= 1
    elif direction == "down":
        x += 1
    elif direction == "left":
        y -= 1
    elif direction == "right":
        y += 1
    return x, y


dimensions = list(map(int, input().split(',')))
matrix = []

rows = dimensions[0]
cols = dimensions[1]
cat_attack = False
cheese = 0
start_row = None
start_col = None

for r in range(rows):
    result = []
    current_row = input()
    for ch in range(len(current_row)):
        if current_row[ch] == 'M':
            start_row = r
            start_col = ch
        elif current_row[ch] == 'C':
            cheese += 1
        result.append(current_row[ch])
    matrix.append(result)

command = input()

while True:
    row, col = mouse_next_position(start_row, start_col, command)

    if row < 0 or row == rows or col < 0 or col == cols:
        cat_attack = True
        break

    if matrix[row][col] == 'C':
        matrix[start_row][start_col] = '*'
        matrix[row][col] = 'M'
        cheese -= 1
        start_row = row
        start_col = col
        if cheese == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            for j in matrix:
                print(f"{''.join(j)}")
            break

    elif matrix[row][col] == "*":
        matrix[start_row][start_col] = '*'
        matrix[row][col] = 'M'
        start_row = row
        start_col = col

    elif matrix[row][col] == 'T':
        matrix[start_row][start_col] = '*'
        matrix[row][col] = 'M'
        start_row = row
        start_col = col
        print('Mouse is trapped!')
        for k in matrix:
            print(f"{''.join(k)}")
        break

    elif matrix[row][col] == '@':
        pass

    elif command == 'danger' and cheese > 0:
        print("Mouse will come back later!")
        for z in matrix:
            print(f"{''.join(z)}")
        break

    command = input()

if cat_attack:
    print("No more cheese for tonight!")
    for i in matrix:
        print(f"{''.join(i)}")
