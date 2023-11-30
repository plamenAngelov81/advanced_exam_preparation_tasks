def team_lineup(*args):
    football_players = {}

    for name, country in args:
        if country not in football_players:
            football_players[country] = [name]
        else:
            football_players[country].append(name)

    sorted_players = dict(sorted(football_players.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ''
    for k, v in sorted_players.items():
        result += f'{k}:\n'
        for name in v:
            result += f"  -{name}\n"

    return result.strip()


print(
    team_lineup(
        ("Harry Kane", "England"),
        ("Manuel Neuer", "Germany"),
        ("Raheem Sterling", "England"),
        ("Toni Kroos", "Germany"),
        ("Cristiano Ronaldo", "Portugal"),
        ("Thomas Muller", "Germany")
    )
)
