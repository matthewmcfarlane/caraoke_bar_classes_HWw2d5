import unittest
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Billy", 47)
        self.song1 = Song('YMCA', 287)
    def test_guest_has_name(self):
        expected = "Billy"
        actual = self.guest.name
        self.assertEqual(expected, actual)

    def test_guest_has_age(self):
        expected = 47
        actual= self.guest.age
        self.assertEqual(expected, actual)

    def test_customer_can_sing_song(self):
        song = self.song1
        result = self.guest.sing_song(song)
        expected = "I am singing YMCA"
        self.assertEqual(expected, result)