from random import *

world_list = ['cat', 'dog', 'umbrella', 'table', 'daughter']


def get_word(list):
    return choice(list).upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
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
    return stages[tries]


word = get_word(world_list)
print(word)


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('''Hello! Let's play in a game...\n''')
    print(display_hangman(6))
    print('You have 6 tries...')
    print(word_completion)
    gess = input('Enter a letter or a word\n').upper()
    for i in gess:
        if not i.isalpha():
            print('You enter something wrong')
    if gess not in word:
        guessed_letters.append(i)
        tries-=1
        print(f'You have {tries} tries')
        print(display_hangman(tries))
        print(guessed_letters)
        #play(word)
    for i in word:
        if gess == word:
            print(word)
            print('Congradulation!!! You are WIN')
            break
        elif i != gess:
            print("_", end="")
        elif i == gess:
            print(gess, end='')





play(word)
