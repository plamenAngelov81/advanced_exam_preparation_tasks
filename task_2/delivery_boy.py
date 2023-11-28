def get_next_position(x, y, direction):
    if direction == "up":
        x -= 1
    elif direction == "down":
        x += 1
    elif direction == "left":
        y -= 1
    elif direction == "right":
        y += 1
    return x, y


rows, cols = list(map(int, input().split(' ')))

neighborhood_field = []
boy_row = None
boy_col = None
restaurant_passed = False
command = ' '

for i in range(rows):
    current_data = input()
    next_row = []
    for j in range(len(current_data)):
        next_row.append(current_data[j])
        if current_data[j] == 'B':
            boy_row = i
            boy_col = j
    neighborhood_field.append(next_row)

start_row = boy_row
start_col = boy_col

while command:
    command = input()

    row, col = get_next_position(start_row, start_col, command)
    if not 0 <= row < rows or not 0 <= col < cols:
        print("The delivery is late. Order is canceled.")
        neighborhood_field[boy_row][boy_col] = ' '
        break

    if neighborhood_field[row][col] == '*':
        continue

    if neighborhood_field[row][col] == 'P':
        neighborhood_field[row][col] = 'R'
        restaurant_passed = True
        start_row, start_col = row, col
        print("Pizza is collected. 10 minutes for delivery.")

    elif neighborhood_field[row][col] == '-':
        neighborhood_field[row][col] = '.'
        start_row, start_col = row, col

    elif neighborhood_field[row][col] == 'A' and restaurant_passed:
        neighborhood_field[row][col] = 'P'
        print("Pizza is delivered on time! Next order...")
        break


for k in neighborhood_field:
    print(f"{''.join(k)}")
