def forecast(*args):

    forecast_dict = {}

    for i in args:
        town = i[0]
        weather = i[1]
        forecast_dict[town] = weather

    sunny = ''
    cloudy = ''
    rainy = ''
    for k, v in sorted(forecast_dict.items(), key=lambda x: (x[1], x[0])):
        if v == 'Rainy':
            rainy += f"{k} - {v}\n"
        elif v == 'Cloudy':
            cloudy += f"{k} - {v}\n"
        elif v == 'Sunny':
            sunny += f"{k} - {v}\n"

    result = sunny + cloudy + rainy

    return result


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))