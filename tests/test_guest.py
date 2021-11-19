import unittest
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Billy", 47)

    def test_guest_has_name(self):
        expected = "Billy"
        actual = self.guest.name
        self.assertEqual(expected, actual)

    def test_guest_has_age(self):
        expected = 47
        actual= self.guest.age
        self.assertEqual(expected, actual)

    def test_customer_can_sing_song(self):
        song = Song('YMCA', 287)
        result = self.guest.sing_song(song)
        expected = "I am singing YMCA"
        self.assertEqual(expected, result)
