class Song:
    def __init__(self, artist, title, album, release_date, price):
        self.artist = artist
        self.title = title
        self.album = album
        self.release_date = release_date
        self.price = price

    def display(self):
        print("--------------------")
        print("Artist:", self.artist)
        print("Song:", self.title)
        print("Album:", self.album)
        print("Release Date:", self.release_date)
        print("Price:", self.price)


# This is outside the Song class
def sort_songs_by_release_date(songs):
    return sorted(
        songs,
        key=lambda song: song.release_date,
        reverse=True
    )