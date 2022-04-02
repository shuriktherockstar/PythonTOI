import math
import random

print("Possible operations: ")
print("\t+\t\tСложение")
print("\t-\t\tВычитание")
print("\t*\t\tУмножение")
print("\t/\t\tДеление")
print("\tСТЕПЕНЬ\t\tВозведение в степень")
print("\tМОДУЛЬ\t\tМодуль числа")
print("\tРАНДОМ\t\tСлучайное число от 0 до 1")
print("\tФАКТОРИАЛ\tФакториал числа")
print("\tАРККОС\t\tАрккосинус")
print("\tВЫЙТИ\t\tВыйти")
while (True):
    operation = str(input("Введите название операции: "))
    if operation == '+':
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} + {} = {}".format(num1, num2, num1 + num2))
    elif operation == '-':
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} - {} = {}".format(num1, num2, num1 - num2))
    elif operation == '/':
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} / {} = {}".format(num1, num2, num1 / num2))
    elif operation == '*':
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} * {} = {}".format(num1, num2, num1 * num2))
    elif operation == 'СТЕПЕНЬ':
        num1 = float(input("Основание: "))
        num2 = float(input("Степень: "))
        print("{} ^ {} = {}".format(num1, num2, num1 ** num2))
    elif operation == 'МОДУЛЬ':
        num = float(input("Число: "))
        print("|{}| = {}".format(num, abs(num)))
    elif operation == 'РАНДОМ':
        print("Случайное число - {}".format(random.random()))
    elif operation == 'ФАКТОРИАЛ':
        num = int(input("Число (только целое и положительное): "))
        print("{}! = {}".format(num, math.factorial(num)))
    elif operation == 'АРККОС':
        num = float(input("Число от -1 до 1: "))
        if (num <= 1) and (num >= -1):
            print("arccos({}) = {}".format(num, math.acos(num)))
        else:
            print("Ошибка!")
    elif operation == 'ВЫЙТИ':
        break
    else:
        print("Нет такой операции")