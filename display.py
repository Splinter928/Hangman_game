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
