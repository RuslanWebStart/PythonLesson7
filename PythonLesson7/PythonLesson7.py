# -*- coding: cp1251  -*-

# ���� 7

# ������ 1
string = input('������� ������: ')
reversString = string[::-1]

if string == reversString:
    print('������ �������� �����������? yes')
else:
    print('������ �������� �����������? no')


# ������ 2
stringX = input('������� ������: ')
resString = ' '.join(stringX.split())

print(f'������ ������������: {resString}')
