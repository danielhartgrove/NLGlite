import unittest

from NLGlite.trainer.wordPair import wordPair


class wordPairTest(unittest.TestCase):
    def test_get_word(self):
        wp1 = wordPair("Dog", "NN")
        self.assertTrue(wp1.get_word() == "Dog")
        self.assertTrue(wp1.get_type() == "NN")

    def test_get_empty(self):
        wp2 = wordPair("", "")
        self.assertTrue(wp2.get_word() == "")
        self.assertTrue(wp2.get_type() == "")


if __name__ == '__main__':
    unittest.main()
