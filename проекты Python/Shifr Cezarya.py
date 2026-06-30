# Шифрофание и дешифрование по Цезарю

print('Приветствую в программе которая может шифровать и дешифровать сообщения по Цезарю:')


def shifr(stp, lng, txt):
    shifrt = ''
    if lng == 'en':
        for i in txt:
            if i.isalpha() and i == i.lower():
                shifrt += chr(ord("a") + (ord(i) - ord("a") + 26 + stp) % 26)
            elif i.isalpha() and i == i.upper():
                shifrt += chr(ord("A") + (ord(i) - ord("A") + 26 + stp) % 26)
            else:
                shifrt += i

    elif lng == 'ру':
        for i in txt:
            if i.isalpha() and i == i.lower():
                shifrt += chr(ord("а") + (ord(i) - ord("а") + 32 + stp) % 32)
            elif i.isalpha() and i == i.upper():
                shifrt += chr(ord("А") + (ord(i) - ord("А") + 32 + stp) % 32)
            else:
                shifrt += i

    return shifrt


def deshifr(stp, lng, txt):
    shifrf = ''
    if lng == 'en':
        for i in txt:
            if i.isalpha() and i == i.lower():
                shifrf += chr(ord("a") + (ord(i) - ord("a") + 26 - stp) % 26)
            elif i.isalpha() and i == i.upper():
                shifrf += chr(ord("A") + (ord(i) - ord("A") + 26 - stp) % 26)
            else:
                shifrf += i

    elif lng == 'ру':
        for i in txt:
            if i.isalpha() and i == i.lower():
                shifrf += chr(ord("а") + (ord(i) - ord("а") + 32 - stp) % 32)
            elif i.isalpha() and i == i.upper():
                shifrf += chr(ord("А") + (ord(i) - ord("А") + 32 - stp) % 32)
            else:
                shifrf += i

    return shifrf

# Этот кусок позволяет прогнать текст и понять с каким шагом его можно расшифровать. Настройки надо вбивать самому.
#text1 = 'Hawnj pk swhg xabkna ukq nqj.'
#for i in range(25):
    print(deshifr(i, 'en', text1))




while True:
    direct = input('Будем шифровать или дешифровать? если Да пиши 1 если нет - 2:  ')
    lang = input('Какой будем использовать язык? Английский - en , Русский - ру: ')
    step = int(input('Какой шаг сдвига будет? Напиши цифру: '))
    text = input('Ну и сюда собственно сам текст: ')
    if direct == '1':
        print(shifr(step, lang, text))
        qwe = input('Хотите ещё раз? Да - 1 , нет - 2: ')
        if qwe == '1':
            continue
        else:
            break


    elif direct == '2':
        print(deshifr(step, lang, text))
        qwes = input('Хотите ещё раз? Да - 1 , нет - 2: ')
        if qwes == '1':
            continue
        else:
             break

