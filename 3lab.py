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
    oper = str(input("Введите имя операции: "))
    if oper == '+':
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} + {} = {}".format(num1, num2, num1 + num2))
    elif oper == '-':
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} - {} = {}".format(num1, num2, num1 - num2))
    elif oper == '*':
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} * {} = {}".format(num1, num2, num1 * num2))
    elif oper == '/':
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} / {} = {}".format(num1, num2, num1 / num2))
    elif oper == 'СТЕПЕНЬ' or oper == 'Степень' or oper == 'степень':
        num1 = float(input("Основание: "))
        num2 = float(input("Степень: "))
        print("{} ^ {} = {}".format(num1, num2, num1 ** num2))
    elif oper == 'МОДУЛЬ' or oper == 'Модуль' or oper == 'модуль':
        num = float(input("Число: "))
        print("|{}| = {}".format(num, abs(num)))
    elif oper == 'РАНДОМ' or oper == 'Рандом' or oper == 'рандом':
        print("Случайное число - {}".format(random.random()))
    elif oper == 'ФАКТОРИАЛ' or oper == 'Факториал' or oper == 'факториал':
        num = int(input("Число (только натуральное и ноль): "))
        if num >= 0:
            print("{}! = {}".format(num, math.factorial(num)))
        else:
            print("Ошибка!")
    elif oper == 'АРККОС' or oper == 'Арккос' or oper == 'арккос':
        num = float(input("Число от -1 до 1: "))
        if (num <= 1) and (num >= -1):
            print("arccos({}) = {}".format(num, math.acos(num)))
        else:
            print("Ошибка!")
    elif oper == 'ВЫЙТИ' or oper == 'Выйти' or oper == 'выйти':
        break
    else:
        print("Нет такой операции!")
