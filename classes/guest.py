class Guest:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sing_song(self, song):
        return f"I am singing {song.name}"