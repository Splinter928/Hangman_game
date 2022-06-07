import string
from display import Display
from words import Word


class Game:

    def __init__(self):
        self.guessed = False  # signal flag1
        self.tries = 6  # number of available tries
        self.word = Word()
        self.hangman = Display()

    def bad_letter(self):
        print('Такой буквы в слове нет. Осталось попыток: %d' % self.tries)
        self.hangman.display_hangman(self.tries)
        print('Слово: ', end='')
        print(*self.word.word_progress)
        print('Ранее введенные буквы:', end=' ')
        print(*sorted(self.word.guessed_letters), sep=', ')
        print()

    def good_letter(self, char):
        print('Такая буква в слове есть!')
        for i in range(len(self.word.word)):
            if char == self.word.word[i]:
                self.word.word_progress[i] = char
        print('Слово: ', end='')
        print(*self.word.word_progress)
        print()

    def bad_word(self):
        print('Слово неверное! Осталось попыток: %d' % self.tries)
        self.hangman.display_hangman(self.tries)
        print('Слово: ', end='')
        print(*self.word.word_progress)
        print('Ранее введенные слова:', end=' ')
        print(*sorted(self.word.guessed_words), sep=', ')
        print()

    def check_start(self, char):
        if not char.isalpha() or char in string.ascii_uppercase:
            print('Вводите русскую букву или слово целиком!')
            return False
        elif char in self.word.guessed_words or char in self.word.guessed_letters:
            print('Вы уже вводили такой вариант! Попробуйте что-то новенькое.')
            return False
        return True

    def check_word(self, current_word):
        if current_word == self.word.word:
            self.guessed = True
        elif current_word != self.word.word:
            self.tries -= 1
            self.word.guessed_words.append(current_word)
            self.bad_word()

    def check_letter(self, current_letter):
        if current_letter not in self.word.word:
            self.tries -= 1
            self.word.guessed_letters.append(current_letter)
            self.bad_letter()
        elif current_letter in self.word.word:
            self.word.guessed_letters.append(current_letter)
            self.good_letter(current_letter)
        if ''.join(self.word.word_progress) == self.word.word:
            self.guessed = True

    def check_finish(self):
        if self.guessed:
            print('%s - правильный ответ! Вы победили!' % self.word.word)
        else:
            print('Слово было - %s. В этот раз не повезло :( Попробуйте снова!' % self.word.word)

    def game(self):

        print(f'Сыграем в виселицу? Доступное количество попыток: {self.tries}')
        self.hangman.display_hangman()
        print(*self.word.word_progress)

        while self.tries > 0 and not self.guessed:
            char = input('Введите букву или слово:\n').upper()
            if not self.check_start(char):
                continue
            elif len(char) > 1:
                self.check_word(char)
                continue
            elif len(char) == 1:
                self.check_letter(char)
                continue

        self.check_finish()


if __name__ == '__main__':
    g = Game()
    g.game()
