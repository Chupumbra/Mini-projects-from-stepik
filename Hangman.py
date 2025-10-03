import random

tries = 6  # количество попыток
word_list = ['МОРЕ', "СЕССИЯ", "УЧЕБА", "КАПКАН", "ВКУС", "КАВКАЗ", "ТЮЛЬПАН"]

def get_word():
    w = random.choice(word_list)
    return w

def display_hangman(tries):
    stages = ['''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ ⎞
                   |
                   -
    ''',
    '''    
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ 
                   |
                   -
    ''',
    '''  
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |
                   |
                   -
    ''',
    '''    
                   --------
                   |      |
                   |      O
                   |     ⎛▼
                   |
                   |
                   -
    ''',
    '''
                   --------
                   |      |
                   |      O
                   |      ▼
                   |
                   |
                   -
    ''',
    '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
    ''',
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

def play(word):
    tries = 6
    word_completion = '_' * len(get_word())  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)

    while not guessed and tries > 0:
        char = input('Введите букву ').upper()

        if not (ord('А') <= ord(char) <= ord('Я')):
            print('Введите корректную букву! ')
            continue

        if char in guessed_letters:
            print('Вы уже называли эту букву! ')
            continue

        guessed_letters.append(char)

        if char in word:
            print(f'Буква {char} есть в слове! ')
            word_completion = ''.join([word[i] if word[i] == char else word_completion[i]
                                       for i in range(len(word))])
        else:
            tries -= 1
            print(f'Буква {char} нет в слове! Осталось попыток: {tries}')
            print(display_hangman(tries))
        print(word_completion)

        if word_completion == word:
            print('Вы угадали слово, вы победили! ')
            guessed = True

    if not guessed:
        print(f'Вы проиграли. Загаданное слово было {word} ')

play(word=get_word())









