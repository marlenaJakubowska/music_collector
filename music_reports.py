# CODECOOL MUSIC LIBRARY

import display
# albums_dict = {artist name, album name, release year, genre, length}


def read_albums(file_path):
    data = []

    with open(file_path) as file:
        lines = file.readlines()
        
    for line in lines:
        splitted_line = line.strip().split(',')
        splitted_line[2] = int(splitted_line[2])
        data.append(splitted_line)
        
    return data

def main():
    path = 'text_albums_data.txt'
    albums = read_albums(path)
    display.print_table(albums)


main()
