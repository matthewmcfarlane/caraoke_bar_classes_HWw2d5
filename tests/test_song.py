import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("YMCA", 287)
    
    def test_song_has_name(self):
        expected = "YMCA"
        actual = self.song.name
        self.assertEqual(expected, actual)

    def test_song_has_duration(self):
        expected = 287
        actual = self.song.duration
        self.assertEqual(expected, actual)

    
