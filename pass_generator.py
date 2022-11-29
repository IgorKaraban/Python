from random import choice

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
count_pas = int(input('Укажите количество паролей для генерации:\n'))
len_pas = int(input('Укажите длинну пароля:\n'))
dig_case = input('Включать цифры?\ny/n\n')
low_case = input('Включать прописные буквы?\ny/n\n')
up_case = input('Включать строчные буквы?\ny/n\n')
char_case = input('Включать символы?\ny/n\n')
str_char_case = input('Исключать ли неоднозначные символы il1Lo0O?\ny/n\n')
if dig_case == 'y':
    chars = chars + digits
if low_case == 'y':
    chars = chars + lowercase_letters
if up_case == 'y':
    chars = chars + uppercase_letters
if char_case == 'y':
    chars = chars + punctuation
if str_char_case.lower() == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(length, chars):
    pas = ''
    for i in range(0, len_pas):
        pas += choice(chars)
    return print(pas)


for i in range(0, count_pas):
    generate_password(len_pas, chars)
