def movie_organizer(*args):
    movie_library = {}
    for i in args:
        movie = i[0]
        genre = i[1]
        if genre not in movie_library:
            movie_library[genre] = [movie]
        else:
            movie_library[genre].append(movie)

    sorted_items = dict(sorted(movie_library.items(), key=lambda x: (-len(x[1]), x[0])))

    result = ''

    for k, v in sorted_items.items():
        result += f'{k} - {len(v)}\n'
        for movie in sorted(v):
            result += f"* {movie}\n"

    return result.strip()


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))