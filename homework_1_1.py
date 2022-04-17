'''
Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python

Практическое задание № 2

https://drive.google.com/file/d/1ZGrz3vsC0gXY5bQCrqTlPAeJBJ9UXiod/view?usp=sharing
'''

n = int(input('Введите любое трехзначное число '))
d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10

print("Сумма цифр числа: ", n + d1 + d2)
print("Произведение цифр числа: ", n * d1 * d2)

