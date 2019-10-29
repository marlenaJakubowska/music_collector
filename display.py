# tu funkcje, które coś printują


def print_table(albums):
    for album in albums:
        print(album)

# album not found
    if len(albums) == 0:
        print("No albums found")
