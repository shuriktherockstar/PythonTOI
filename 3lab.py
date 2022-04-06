import math
import random

print("\tИмя\t\t\tДействие")
print()
print("\t+\t\t\tСложение")  # \t - отступ
print("\t-\t\t\tВычитание")
print("\t*\t\t\tУмножение")
print("\t/\t\t\tДеление")
print("\tСТЕПЕНЬ\t\tВозведение в степень")
print("\tМОДУЛЬ\t\tМодуль числа")
print("\tРАНДОМ\t\tСлучайное число от 0 до 1")
print("\tФАКТОРИАЛ\tФакториал числа")
print("\tАРККОС\t\tАрккосинус")
print("\tВЫЙТИ\t\tВыйти")

while True:
    operation = str(input("Введите имя операции: "))
    if operation == '+':
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} + {} = {}".format(num1, num2, num1 + num2))
    elif operation == '-':
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} - {} = {}".format(num1, num2, num1 - num2))
    elif operation == '*':
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} * {} = {}".format(num1, num2, num1 * num2))
    elif operation == '/':
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} / {} = {}".format(num1, num2, num1 / num2))
    elif operation == 'СТЕПЕНЬ' or operation == 'Степень' or operation == 'степень':
        num1 = float(input("Основание: "))
        num2 = float(input("Степень: "))
        print("{} ^ {} = {}".format(num1, num2, num1 ** num2))
    elif operation == 'МОДУЛЬ' or operation == 'Модуль' or operation == 'модуль':
        num = float(input("Число: "))
        print("|{}| = {}".format(num, abs(num)))
    elif operation == 'РАНДОМ' or operation == 'Рандом' or operation == 'рандом':
        print("Случайное число - {}".format(random.random()))
    elif operation == 'ФАКТОРИАЛ' or operation == 'Факториал' or operation == 'факториал':
        num = int(input("Число (только натуральное и ноль): "))
        if num >= 0:
            print("{}! = {}".format(num, math.factorial(num)))
        else:
            print("Ошибка!")
    elif operation == 'АРККОС' or operation == 'Арккос' or operation == 'арккос':
        num = float(input("Число от -1 до 1: "))
        if (num <= 1) and (num >= -1):
            print("arccos({}) = {}".format(num, math.acos(num)))
        else:
            print("Ошибка!")
    elif operation == 'ВЫЙТИ' or operation == 'Выйти' or operation == 'выйти':
        break
    else:
        print("Нет такой операции!")
