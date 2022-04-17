'''
Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python

Практическое задание № 8

https://drive.google.com/file/d/1ZGrz3vsC0gXY5bQCrqTlPAeJBJ9UXiod/view?usp=sharing
'''

year = int(input('Введите любой год: '))

if (year %  4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Год является високосным')
else:
    print('Год является НЕ високосным')