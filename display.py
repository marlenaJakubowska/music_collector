# tu funkcje, które coś printują
import music_reports
# print table


def print_table(albums):
    print("-" * 101 + "\n" + " | ".join(("artist name".center(30), "album name".center(30), "year".center(4), "genre".center(18), "length".center(6))) + "\n" + "-" * 101)

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


def print_statistics(data):

    longest_albums = music_reports.find_longest_album(data)
    longest_albums_to_print = ""
    for album in longest_albums:
        longest_albums_to_print += str(album[1]) + ", "
    longest_albums_to_print += " Length: " + str(longest_albums[0][-1])

    shortest_albums = music_reports.find_shortest_album(data)
    shortest_albums_to_print = ""
    for album in shortest_albums:
        shortest_albums_to_print += str(album[1]) + ", "
    shortest_albums_to_print += " Length: " + str(shortest_albums[0][-1])

    oldest_albums = music_reports.find_oldest_album(data)
    oldest_albums_to_print = ""
    for album in oldest_albums:
        oldest_albums_to_print += str(album[1]) + ", "
    oldest_albums_to_print += " Year: " + str(oldest_albums[0][2])

    youngest_albums = music_reports.find_newest_album(data)
    youngest_albums_to_print = ""
    for album in youngest_albums:
        youngest_albums_to_print += str(album[1]) + ", "
    youngest_albums_to_print += " Year: " + str(youngest_albums[0][2])

    all_albums_count = str(len(data))
    additional_info = "to_be_implemented"

    print()
    print("Longest album: " + longest_albums_to_print)
    print("Shortest album: " + shortest_albums_to_print)
    print("Oldest album: " + oldest_albums_to_print)
    print("Youngest album: " + youngest_albums_to_print)
    print("All albums count: " + all_albums_count)
    print("Additional info: " + additional_info)
    print()
