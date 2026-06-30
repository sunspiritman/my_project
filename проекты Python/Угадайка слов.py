# Угадайка слов

import random

word = ['планета', 'пёс', 'картина', 'окно', 'природа', 'солнце', 'радость', 'мыкало', 'мяукало']

# Функция которая возвращает рандомно слово из списка word
def get_world():
    return random.choice(word).upper()

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

# Здесь основная логика игры
def play():
    tr = 6
    rworld = get_world()
    word_completion = list('_' * len(rworld))  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    print("Давай сыграем в игру под названием 'Угадайка слов'. Ты должен угадывать буквы этого слова либо ввести слово целиком. Поехали!")
    print(f'У тебя есть {tr} попыток и твоя висилица на начально уровне выглядит так:\n{display_hangman(tr)}')
    print(f'И так, есть слово и оно состоит из {len(rworld)} букв')

    while tr != 0:
        l = input('Введи русскую букву или слово: ').upper()
        if not l.isalpha():
            print('Нужно ввести русскую букву или слово.')
            continue

        elif len(l) > 1:
            if l in guessed_words:
                print('Это слово вы уже вводили.')
            elif l == rworld:
                print('Поздравляем, вы угадали слово! Вы победили!')
            elif l != rworld:
                guessed_words.append(l)
                tr -= 1
                print(f'Не верно! У вас осталось {tr} попыток.\nСлово: {''.join(word_completion)}\n{display_hangman(tr)}')


        elif len(l) == 1:
            if l in guessed_letters:
                print('Эту букву вы уже вводили.')
            elif l in rworld:
                guessed_letters.append(l)
                for i in range(len(rworld)):
                    if rworld[i] == l:
                        word_completion[i] = l
                if rworld == ''.join(word_completion):
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    print("Загаданное слово:", ''.join(word_completion))
                    break
                else:
                    print(f'Здесь есть такая буква - {''.join(word_completion)}')

            elif l not in rworld:
                guessed_letters.append(l)
                tr -= 1
                print(f'Не верно! У вас осталось {tr} попыток\nСлово: {''.join(word_completion)}\n{display_hangman(tr)}')


        if tr == 0:
            print(f'Вы проиграли! Правильное слово {rworld}')


play()

while True:
    qw = input('Хотите сыграть ещё раз? да - 1 , нет - 2 : ')
    if qw == '1':
        play()
    else:
        print('Всего хорошего')
        break

