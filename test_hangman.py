import unittest

from words import Word
from display import Display
from hangman import Game


class TestWord(unittest.TestCase):
    """test for class Word in Hangman game"""
    def setUp(self) -> None:
        self.wordobj = Word()
        self.wordobj.word = self.wordobj.get_word().lower()

    def test_word_from_list(self):
        self.assertIn(self.wordobj.word, self.wordobj.words)

    def test_word_is_russian(self):
        word_letters = [let for let in self.wordobj.word]
        russian_unicode = [number for number in range(1072, 1106)]
        for letter in word_letters:
            self.assertIn(ord(letter), russian_unicode)


class TestGame(unittest.TestCase):
    """tests for main class Game in Hangman game"""
    def setUp(self) -> None:
        self.gameobj = Game()

    def test_game_init(self):
        self.assertEqual(self.gameobj.tries, 6)
        self.assertIsInstance(self.gameobj.word, Word)
        self.assertIsInstance(self.gameobj.hangman, Display)


if __name__ == '__main__':
    unittest.main()
