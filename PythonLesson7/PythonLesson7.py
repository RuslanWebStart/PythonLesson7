# -*- coding: cp1251  -*-

# Урок 7

# Задача 1
string = input('Введите строку: ')
reversString = string[::-1]

if string == reversString:
    print('Строка является палиндромом? yes')
else:
    print('Строка является палиндромом? no')


# Задача 2
stringX = input('Введите строку: ')
resString = ' '.join(stringX.split())

print(f'Строка обработанная: {resString}')
