
def print_table(albums):
    print("-" * 101 + "\n" + " | ".join(("artist name".center(30), "album name".center(30), "year".center(4), "genre".center(18), "length".center(6))) + "\n" + "-" * 101)

    for artist_name, album_name, release_year, genre, length in albums:
        print(' | '.join((artist_name.ljust(30), album_name.ljust(30), str(release_year).ljust(4), genre.ljust(18), length.ljust(6))))
    print('-' * 101)

# album not found
    if len(albums) == 0:
        print("No albums found")
