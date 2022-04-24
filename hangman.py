import string
from random import choice


class Display:

    def __init__(self):
        self.condition = 6

    def display_hangman(self, stage_number=6):
        self.condition = stage_number
        stages = [
            # final stage - head, body, 2 arms and 2 legs
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            ''',
            # head, body, 2 arms and 1 leg
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            ''',
            # head, body and 2 arms
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            ''',
            # head, body and 1 arm
            '''
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            ''',
            # head and body
            '''
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            ''',
            # head
            '''
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            ''',
            # starting condition
            '''
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            '''
        ]
        print(stages[self.condition])


class Word:

    def __init__(self):
        with open('words.txt', encoding='utf-8') as f:
            self.words = [w.strip() for w in f.readlines()]
        self.word = choice(self.words).upper()  # random word from file
        self.letters = set(self.word)
        self.word_progress = ['.' for _ in range(len(self.word))]
        self.guessed_letters = []
        self.guessed_words = []

    def get_word(self):
        return self.word


class Game:

    def __init__(self):
        self.guessed = False  # signal flag
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

    def game(self):

        print(f'Сыграем в виселицу? Доступное количество попыток: {self.tries}')
        self.hangman.display_hangman()
        print(*self.word.word_progress)

        while self.tries > 0:
            char = input('Введите букву или слово:\n').upper()

            if not char.isalpha() or char in string.ascii_uppercase:
                print('Вводите русскую букву или слово целиком!')
                continue
            elif char in self.word.guessed_words or char in self.word.guessed_letters:
                print('Вы уже вводили такой вариант! Попробуйте что-то новенькое.')
                continue
            elif len(char) > 1 and char == self.word.word:
                self.guessed = True
                break
            elif len(char) > 1 and char != self.word.word:
                self.tries -= 1
                self.word.guessed_words.append(char)
                self.bad_word()
                continue
            elif len(char) == 1 and char not in self.word.word:
                self.tries -= 1
                self.word.guessed_letters.append(char)
                self.bad_letter()
                continue
            elif len(char) == 1 and char in self.word.word:
                self.word.guessed_letters.append(char)
                self.good_letter(char)

                if ''.join(self.word.word_progress) == self.word.word:
                    self.guessed = True
                    break
                else:
                    continue

        if self.guessed:
            print('%s - правильный ответ! Вы победили!' % self.word.word)
        else:
            print('Слово было - %s. В этот раз не повезло :( Попробуйте снова!' % self.word.word)


if __name__ == '__main__':
    is_game = 'да'
    while is_game.lower() == 'да' or is_game.lower() == 'lf':
        g = Game()
        g.game()
        is_game = input('Хотите попробовать снова? Введите "да", чтобы продолжить или "нет" для выхода.\n')
