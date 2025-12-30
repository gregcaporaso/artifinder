import unittest

from artifinder import main

class ArtifinderTests(unittest.TestCase):

    def test_main(self):
        actual = main()
        self.assertEqual(actual, 0)
