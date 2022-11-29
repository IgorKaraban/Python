from random import *

print('Введите максимальное число')
x = int(input())
num = randrange(x + 1)
print('Добро пожаловать в числовую угадайку')
count = 0


def is_valid(num):
    if 1 <= num <= x:
        return True
    else:
        return False


while True:
    print(f'Enter your number from 1 till {x}')
    user_num = int(input())
    count += 1
    is_valid(user_num)
    if is_valid(user_num) == False:
        print(f'А может быть все-таки введем целое число от 1 до {x}?')
        continue
    if user_num < num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif user_num > num:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif user_num == num:
        print('Вы угадали, поздравляем!')
        print(f'Вы потратили {count} попыток')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        print('Начать новую игру? y-да, n-нет')
        new_game = input()
        if new_game == 'y':
            print('Введите максимальное число')
            x = int(input())
            num = randrange(x + 1)
            count = 0
            print(num, 'Добро пожаловать в числовую угадайку')
            continue
        else:
            break
