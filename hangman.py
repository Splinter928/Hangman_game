from random import choice


class Display:

    def __init__(self):
        self.condition = 6

    def display_hangman(self, stage_number = 6):
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
        self.word_progress = [self.word[i] if i in [0, len(self.word)-1] else '.' for i in range(len(self.word))]
        self.guessed_letters = []
        self.guessed_words = []

    def get_word(self):
        return self.word


class Game:

    def __init__(self):
        self.guessed = False  # signal flag
        self.tries = 6 # number of available tries

    def game(self):
        word = Word()
        hangman = Display()

        print(f'Сыграем в виселицу? Доступное количество попыток: {self.tries}')
        hangman.display_hangman()
        print(*word.word_progress)

        while self.tries > 0:
            char = input('Введите букву или слово:\n').upper()


g = Game()
g.game()