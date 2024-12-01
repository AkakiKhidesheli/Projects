import json


class Songs:
    def __init__(self, name, artist, album, release_year):
        self.name = name
        self.artist = artist
        self.album = album
        self.release_year = release_year

    def __repr__(self):
        bright_ube = '\033[38;2;214;162;232m'
        reset = '\033[0m'
        return f'{bright_ube}Song Name:{reset} {self.name}, {bright_ube}Artist:{reset} {self.artist}, {bright_ube}Album:{reset} {self.album}, {bright_ube}Release Year:{reset} {self.release_year}'


class SongManager:
    def __init__(self):
        self.songs = []
        self.years = {}
        self.albums = {}
        self.artists = {}
        self.sarawak_white_pepper = '\033[38;2;248;239;186m'
        self.clear_chill = '\033[38;2;27;156;252m'
        self.yellow = '\033[93m'
        self.light_blue = '\033[96m'
        self.green = '\033[92m'
        self.bright_ube = '\033[38;2;214;162;232m'
        self.reset = '\033[0m'

    def adding(self, element1, element2, element3):
        if element1 not in element2:
            element2[element1] = [element3]
        else:
            element2[element1].append(element3)

    def adding_year(self, release_year, name):
        self.adding(release_year, self.years, name)

    def adding_album(self, album, name):
        self.adding(album, self.albums, name)

    def adding_artist(self, artist, name):
        self.adding(artist, self.artists, name)

    # def adding_year(self, release_year, name):
    #     if release_year not in self.years:
    #         self.years[release_year] = [name]
    #     else:
    #         self.years[release_year].append(name)

    # def adding_album(self, album, name):
    #     if album not in self.albums:
    #         self.albums[album] = [name]
    #     else:
    #         self.albums[album].append(name)

    # def adding_artist(self, artist, album):
    #     if artist not in self.artists:
    #         self.artists[artist] = [album]
    #     else:
    #         self.artists[artist].append(album)

    def add_songs(self, name, artist, album, release_year):
        song = Songs(name, artist, album, release_year)
        self.songs.append(song)
        self.adding_year(release_year, name)
        self.adding_album(album, name)
        self.adding_artist(artist, name)

    def show_songs(self):
        for song in self.songs:
            print(song)

    def printing(self, element6, text):
        for element4, element5 in element6.items():
            print(f'{text} {self.bright_ube}{element4}{self.reset}: {element5}')

    def show_years(self):
        self.printing(self.years, 'Released songs in')

    def show_albums(self):
        self.printing(self.albums, 'Songs in album')

    def show_artists(self):
        self.printing(self.artists, 'Songs by')

    # def show_years(self):
    #     for year, song in self.years.items():
    #         print(f'Released songs in {year}: {song}')

    # def show_albums(self):
    #     for album, song in self.albums.items():
    #         print(f'Songs in album "{album}" : {song}')

    # def show_artists(self):
    #     for artist, song in self.artists.items():
    #         print(f'Songs by "{artist}" : {song}')

    def printing_individual(self, element7, element8, text):
        if element7 in element8:
            print(f'{text} {element7} : {element8[element7]}')

    def show_year(self, year):
        self.printing_individual(year, self.years, 'Released songs in')

    def show_album(self, album):
        self.printing_individual(album, self.albums, 'Songs in album')

    def show_artist(self, artist):
        self.printing_individual(artist, self.artists, 'Songs by')

    # def show_year(self, year):
    #     if year in self.years:
    #         print(f'Released songs in {year} : {self.years[year]}')

    # def show_album(self, album):
    #     if album in self.albums:
    #         print(f'Songs in {album} : {self.albums[album]}')

    # def show_artist(self, artist):
    #     if artist in self.artists:
    #         print(f'Songs by {artist} : {self.artists[artist]}')

    def search_song(self, name):
        for song in self.songs:
            if song.name.lower() == name.lower():
                print(song)
                return
        print(f'{name} not found')

    def coloring(self, digit, text):
        print(f"{self.sarawak_white_pepper}{digit}{self.reset} {self.clear_chill}{text}{self.reset}")

    def display_menu(self):
        print(f"\n{self.green}\tWelcome to the Song Manager 📀{self.reset}")
        print(f"{self.yellow}This application helps you manage songs.{self.reset}\n")
        print(f"You can perform actions:")
        self.coloring(1, 'Add a new song')
        self.coloring(2, 'View all songs')
        self.coloring(3, 'View all years')
        self.coloring(4, 'View all albums')
        self.coloring(5, 'View all artists')
        self.coloring(6, 'Search for a song and see full info')
        self.coloring(7, 'View song released on a particular year')
        self.coloring(8, 'View songs of a particular album')
        self.coloring(9, 'View songs by particular artist')
        print(f"\n{self.green}For closing, please input 0{self.reset}\n")

    def check_if_exists(self, element8, element9, text, func):
        if element8 not in element9:
            print(f'{text} not found')
        else:
            func(element8)

    def user_action(self):
        self.display_menu()
        while True:
            try:
                keyword = int(input(f"{self.yellow}Please enter 0-9:{self.reset} "))

                if keyword == 1:
                    name = input("Enter song name: ")
                    artist = input("Enter artist name: ")
                    album = input("Enter album name: ")
                    release_year = int(input("Enter release year: "))
                    self.add_songs(name, artist, album, release_year)
                    print("Song added successfully!\n")

                elif keyword == 2:
                    self.show_songs()
                    print()

                elif keyword == 3:
                    self.show_years()
                    print()

                elif keyword == 4:
                    self.show_albums()
                    print()

                elif keyword == 5:
                    self.show_artists()
                    print()

                elif keyword == 6:
                    name = input("Enter song name: ")
                    self.search_song(name)
                    print()

                elif keyword == 7:
                    year = int(input("Enter the year: "))
                    self.check_if_exists(year, self.years, 'Year', self.show_year)
                    print()

                elif keyword == 8:
                    album = input("Enter the album: ")
                    self.check_if_exists(album, self.albums, 'Album', self.show_album)
                    print()

                elif keyword == 9:
                    artist = input("Enter the artist name: ")
                    self.check_if_exists(artist, self.artists, 'Artist', self.show_artist)
                    print()


                elif keyword == 0:
                    songs_data = []
                    for song in self.songs:
                        song_info = {
                            'Song Name': song.name,
                            'Artist': song.artist,
                            'Album': song.album,
                            'Release Year': song.release_year
                        }
                        songs_data.append(song_info)

                    filename = input('Please input file name: ')
                    with open(f'{filename}.json', 'w') as writable_file:
                        json.dump(songs_data, writable_file, indent=4)
                    print(f'{self.green}All of the songs are written in {filename}.json which you can read anytime. '
                          f'\nThank you for using our app. Goodbye!{self.reset}')
                    break

                else:
                    print("Please enter a number between 1 and 7.")
            except ValueError:
                print("Please enter a valid number.")


rock_songs = SongManager()
rock_songs.add_songs("Sweet Child O' Mine", "Guns N' Roses", 'Appetite for Destruction', 1988)
rock_songs.add_songs('Another Brick in the Wall (Part II)', 'Pink Floyd', 'The Wall', 1980)
rock_songs.add_songs("Livin' On a Prayer", 'Bon Jovi', 'Slippery When Wet', 1986)
rock_songs.add_songs('Bohemian Rhapsody', 'Queen', 'A Night at the Opera', 1975)
rock_songs.add_songs('Welcome to the Jungle', "Guns N' Roses", 'Appetite for Destruction', 1987)
rock_songs.add_songs('Love of My Life', 'Queen', 'A Night at the Opera', 1975)
rock_songs.add_songs('Dosed', 'Red Hot Chili Peppers', 'By the Way', 2003)

rock_songs.user_action()
