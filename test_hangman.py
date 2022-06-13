import string
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

    def test_check_start(self):
        printable = r'012345678ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        for char in printable:
            self.assertFalse(self.gameobj.check_start(char))

        self.gameobj.word.guessed_letters = [c for c in 'ПРИМЕР']
        for char in self.gameobj.word.guessed_letters:
            self.assertFalse(self.gameobj.check_start(char))

        self.gameobj.word.guessed_words = 'ТЕСТ'
        self.assertFalse(self.gameobj.check_start(self.gameobj.word.guessed_words))

    def test_check_finish(self):
        self.gameobj.guessed = True
        self.assertTrue(self.gameobj.check_finish())
        self.gameobj.guessed = False
        self.assertFalse(self.gameobj.check_finish())


if __name__ == '__main__':
    unittest.main()
