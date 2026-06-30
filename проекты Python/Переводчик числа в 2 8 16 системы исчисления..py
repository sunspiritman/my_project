def change_10_in(num):
    bin_num = bin(num)
    oct_num = oct(num)
    hex_num = hex(num)
    print(f'В двоичной системе число {num} будет равно {bin_num[2:]}')
    print(f'В восьмеричной системе число {num} будет равно {oct_num[2:]}')
    print(f'В шестнадцатеричной системе число {num} будет равно {hex_num[2:].upper()}')

while True:
    n = input("Введите цифру, которую надо представить в других системах исчисления или слово 'нет', если хотите выйти: ")
    if n.isdigit():
        change_10_in(int(n))
    else:
        print('Всего хорошего.')
        break

