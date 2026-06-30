import random

def rand_digit():
    qwes = input()
    global nums
    global digit
    if not qwes.isdigit() and qwes == '':
        print('Необходимо ввести целое число, попробуйте ещё раз.')
    elif qwes == '2':
        digit = random.randint(1, 100)

    elif qwes == '1':
        nums = input('Введите число до которого будем угадывать: ')
        if not nums.isdigit() and nums == '':
            print('Необходимо ввести целое число, попробуйте ещё раз.')
        elif nums.isdigit():
            nums = int(nums)
            digit = random.randint(1, int(nums))

    return digit


def is_valid(n):
    if not n.isdigit():
        return False
    return 1 <= int(n) <= 100



def osn_cod():
    print('Добро пожаловать в числовую угадайку! Хотите задать число до которого будем угадывать? Если да - 1, нет - 2: ')
    rand_digit()
    num = input(f'Поехали! Теперь введите число от 1 до {nums} включительно, либо Enter если хотите выйти: ')
    kpop = 0
    while True:
        if num == '':
            break

        elif not is_valid(num):
            print(f'А может быть все-таки введем целое число от 1 до {nums}')

        elif is_valid(num):
            num = int(num)
            if num == digit:
                kpop += 1
                print(f'Вы угадали, поздравляем! У вас ушло {kpop} попыток')
                break

            elif num > digit:
                print('Ваше число больше загаданного, попробуйте еще разок')
                kpop += 1

            elif num < digit:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                kpop += 1

        num = input()






osn_cod()

while True:
    reload = input('Хотите сыграть ещё раз? Если да - 1 , нет - 2: ')
    if reload == '2':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
    else:
        osn_cod()

