def accommodate_new_pets(hotel_capacity, weight_limit, *args):
    pets = {}
    result = []

    for pet_type, pet_weight in args:
        if hotel_capacity == 0:
            result.append('You did not manage to accommodate all pets!')
            break

        if weight_limit >= pet_weight:
            if pet_type not in pets:
                pets[pet_type] = 0
            pets[pet_type] += 1
            hotel_capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {hotel_capacity}.")

    result.append('Accommodated pets:')

    for k, v in sorted(pets.items()):
        result.append(f'{k}: {v}')

    return '\n'.join(result)


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
