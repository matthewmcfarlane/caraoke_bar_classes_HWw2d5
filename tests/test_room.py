import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room('CodeClanCaraoke')
        self.guest1 = Guest('Ross', 37)
        self.guest2 = Guest('Matt', 25)
        self.guest3 = Guest('Lara', 27)
        self.song1 = Song('YMCA', 287)
        self.song2 = Song('A short song', 100)
        self.song3 = Song('A long song', 390)
    def test_room_has_name(self):
        expected = 'CodeClanCaraoke'
        actual = self.room.name
        self.assertEqual(expected, actual)

    def test_can_add_guest(self):
        guest1 = Guest('James', 34)
        self.room.add_guest(guest1)
        self.assertIn(guest1, self.room.guests)

    def test_guest_count(self):
        self.room.add_guest(self.guest1)
        self.room.add_guest(self.guest2)
        self.room.add_guest(self.guest3)
        expected = 3
        actual = self.room.guest_count()
        self.assertEqual(expected, actual)
    
    def test_can_remove_guest(self):
        self.room.add_guest(self.guest1)
        self.room.add_guest(self.guest2)
        self.room.add_guest(self.guest3)
        self.room.remove_guest(self.guest1)
        self.assertNotIn(self.guest1, self.room.guests)

    def test_empty_room(self):
        self.room.add_guest(self.guest1)
        self.room.add_guest(self.guest2)
        self.room.add_guest(self.guest3)
        self.room.empty_room()
        expected = 0
        actual = self.room.guest_count()
        self.assertEqual(expected, actual)


    
    def test_can_add_song(self):
        song = self.song1
        self.room.add_song(self.song1)
        self.assertIn(self.song1, self.room.songs)
    

    def test_can_remove_song(self):
        self.room.add_song(self.song1)
        self.room.add_song(self.song2)
        self.room.add_song(self.song3)
        self.room.remove_song(self.song2)
        self.assertNotIn(self.song2, self.room.songs)

    def test_song_count(self):
        self.room.add_song(self.song1)
        self.room.add_song(self.song2)
        self.room.add_song(self.song3)
        expected = 3
        actual = self.room.song_count()
        self.assertEqual(expected, actual)

    def test_remove_all_songs(self):
        self.room.add_song(self.song1)
        self.room.add_song(self.song2)
        self.room.add_song(self.song3)
        self.room.remove_all_songs()
        self.assertEqual(0, self.room.song_count())