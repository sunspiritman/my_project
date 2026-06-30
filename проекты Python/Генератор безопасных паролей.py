import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

n = int(input('Введите количество паролей для генерации цифрой: '))
dlina_p = int(input('Введите длину одного пароля цифрой: '))
isdig = input('Включать ли цифры 0123456789?, Если да, то введите - д если нет - н: ').lower()
upp_p = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Если да, то введите - д если нет - н: ').lower()
low_p = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Если да, то введите - д если нет - н: ').lower()
sym_p = input('Включать ли символы !#$%&*+-=?@^_?. Если да, то введите - д если нет - н: ').lower()
symisk = input('Исключать ли неоднозначные символы il1Lo0O Если да, то введите - д если нет - н: ').lower()

if isdig == 'д':
    chars += digits
if upp_p == 'д':
    chars += uppercase_letters
if low_p == 'д':
    chars += lowercase_letters
if sym_p == 'д':
    chars += punctuation
if symisk == 'д':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

def generate_password(dlina_p, chars):
    for _ in range(n):
        pas = random.sample(chars, dlina_p)
        print(*pas, sep='')

generate_password(dlina_p, chars)
