from collections import deque

size = 6

matrix = []
water = 0
metal = 0
concrete = 0

for _ in range(size):
    matrix.append(list(input().split()))

rover_row = 0
rover_col = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "E":
            rover_row = row
            rover_col = col

directions = deque(input().split(", "))


def examine(rover_row, rover_col, t):
    global water
    global metal
    global concrete
    if t == "W":
        water += 1
        print(f"Water deposit found at ({rover_row}, {rover_col})")
    elif t == "M":
        metal += 1
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
    elif t == "C":
        concrete += 1
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
    elif t == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        return True
    return False


while directions:
    current_direction = directions.popleft()
    if current_direction == "right":
        rover_col += 1
        if rover_col == size:
            rover_col = 0
    elif current_direction == "left":
        rover_col -= 1
        if rover_col < 0:
            rover_col = size - 1
    elif current_direction == "down":
        rover_row += 1
        if rover_row == size:
            rover_row = 0
    elif current_direction == "up":
        rover_row -= 1
        if rover_row < 0:
            rover_row = size - 1
    if examine(rover_row, rover_col, matrix[rover_row][rover_col]):
        break

if water >= 1 and metal >= 1 and concrete >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
