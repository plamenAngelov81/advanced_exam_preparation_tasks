from collections import deque
num_str = input().split(", ")
numbers_1 = deque(input().split(", "))
numbers_2 = input().split(", ")

rotations = 0
seat_matches = []
while numbers_1 and numbers_2:
    num_1 = numbers_1.popleft()
    num_2 = numbers_2.pop()
    current_sum = int(num_1) + int(num_2)
    current_letter = chr(current_sum)
    str_1 = str(num_1) + current_letter
    str_2 = str(num_2) + current_letter
    if str_1 in num_str:
        seat_matches.append(str_1)
        num_str.remove(str_1)
    elif str_2 in num_str:
        seat_matches.append(str_2)
        num_str.remove(str_2)
    else:
        numbers_1.append(num_1)
        numbers_2.insert(0, num_2)
    rotations += 1
    if rotations == 10 or len(seat_matches) == 3:
        break

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")
