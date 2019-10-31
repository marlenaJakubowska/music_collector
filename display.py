
def print_table(albums):
    print("-" * 101 + "\n" + " | ".join(("\033[32m" + "artist name".center(30) + "\033[0m", "\033[32m" + "album name".center(30) + "\033[0m", "\033[32m" + "year".center(4) + "\033[0m", "\033[32m" + "genre".center(18) + "\033[0m", "\033[32m" + "length".center(6) + "\033[0m")) + "\n" + "-" * 101)

    for artist_name, album_name, release_year, genre, length in albums:
        print(' | '.join((artist_name.ljust(30), album_name.ljust(30), str(release_year).ljust(4), genre.ljust(18), length.ljust(6))))
    print('-' * 101)

# album not found
    if len(albums) == 0:
        print("No albums found")


def choose_option():
    available_options = [
        "1: I want to view all imported albums",
        "2: I want to find all albums by genre",
        "3: I want to find all albums from given time range",
        "4: I want to find shortest/longest album",
        "5: I want to find all albums created by given artist",
        "6: I want to find album by album name",
        "7: I want to get full report in form of set of given statistics",
        "add: Add new album",
        "q: Quit",
    ]
    for option in available_options:
        print(option)
    user_option = input("\nPlease enter option: ")
    return user_option.lower()
