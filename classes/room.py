class Room:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.guests = []

    def add_guest(self, guest):
        self.guests.append(guest)
    
    def guest_count(self):
        return len(self.guests)
    
    def remove_guest(self, guest):
        self.guests.remove(guest)

    def empty_room(self):
        self.guests.clear()


    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)
    
    def song_count(self):
        return len(self.songs)

    def remove_all_songs(self):
        self.songs.clear()
    

    