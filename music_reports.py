# CODECOOL MUSIC LIBRARY

import display

#  data = {"artist name", "album name", "release year", "genre", "length"}
# genre = "rock"


def choose_option():
    available_options = [
        "1: I want to view all imported albums",
        "2: I want to find all albums by genre",
        "3: I want to find all albums from given time range",
        "4: I want to find shortest/longest album",
        "5: I want to find all albums created by given artist",
        "6: I want to find album by album name",
        "7: I want to get full report in form of set of given statistics",
        "q: Quit"
    ]
    for option in available_options:
        print(option)
    user_option = input("Please enter option: ")
    return user_option


def read_albums(file_path):
    data = []

    with open(file_path) as file:
        lines = file.readlines()

    for line in lines:
        splitted_line = line.strip().split(',')
        splitted_line[2] = int(splitted_line[2])
        data.append(splitted_line)

    return data


def find_albums_by_genre(genre, data):
    filtered_albums = []
    for album in data:
        if genre in album[3]:
            filtered_albums.append(album)
    return filtered_albums


def find_albums_by_time_range(data, from_time, to_time):
    filtered_albums = []
    for album in data:
        if album[2] >= from_time and album[2] <= to_time:
            filtered_albums.append(album)
    return filtered_albums


def input_time_range():
    incorrect_from_time = True
    incorrect_to_time = True

    while incorrect_from_time:
        from_time = input("Please enter from year: ")

        try:
            if from_time == "":
                from_time = 0

            from_time = int(from_time)
            incorrect_from_time = False
        except ValueError:
            print("Please enter correct number")

    while incorrect_to_time:
        to_time = input("Please enter to year: ")
        try:
            if to_time == "":
                to_time = 3000
            to_time = int(to_time)
            if from_time > to_time:
                raise ValueError

            incorrect_to_time = False
        except ValueError:
            print("Please enter correct number")

    return from_time, to_time


def find_albums_by_artist(artist, data):
    filtered_albums = []
    for album in data:
        if artist in album[0]:
            filtered_albums.append(album)
    return filtered_albums


def find_albums_by_name(name, data):
    filtered_albums = []
    for album in data:
        if name in album[1]:
            filtered_albums.append(album)
    return filtered_albums


def main():
    # todo: user should be able to stay in program after choosing option
    path = 'text_albums_data.txt'
    albums = read_albums(path)
    # option = choose_option()
    is_running = True

    while is_running:

        option = choose_option()

        if option == "1":
            display.print_table(albums)

        elif option == "2":
            filtered_albums_by_genre = find_albums_by_genre(input("What type of genre do you want to find? "), albums)
            display.print_table(filtered_albums_by_genre)

        elif option == "3":
            from_time, to_time = input_time_range()
            filtered_albums_by_time_range = find_albums_by_time_range(
                albums, from_time, to_time)
            display.print_table(filtered_albums_by_time_range)

        elif option == "5":
            filtered_albums_by_artist = find_albums_by_artist(input("Which artist do you want to find? ").title(), albums)
            display.print_table(filtered_albums_by_artist)

        elif option == "6":
            filtered_albums_by_name = find_albums_by_name(input("Which album do you want to find? ").title(), albums)
            display.print_table(filtered_albums_by_name)

        elif option == "q" or "Q":
            is_running = False


main()
