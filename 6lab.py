import math
import random


def Information():
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


def Sum():
    num1 = float(input("Первое число: "))
    num2 = float(input("Второе число: "))
    print("{} + {} = {}".format(num1, num2, num1 + num2))


def Subtraction():
    num1 = float(input("Первое число: "))
    num2 = float(input("Второе число: "))
    print("{} - {} = {}".format(num1, num2, num1 - num2))


def Multiplication():
    num1 = float(input("Первое число: "))
    num2 = float(input("Второе число: "))
    print("{} * {} = {}".format(num1, num2, num1 * num2))


def Division():
    num1 = float(input("Делимое: "))
    num2 = float(input("Делитель: "))
    print("{} * {} = {}".format(num1, num2, num1 / num2))


def Power():
    num1 = float(input("Основание: "))
    num2 = float(input("Степень: "))
    print("{} ^ {} = {}".format(num1, num2, num1 ** num2))


def Abs():
    num = float(input("Число: "))
    print("|{}| = {}".format(num, abs(num)))


def Random():
    print("Случайное число - {}".format(random.random()))


def Factorial():
    num = int(input("Число (только натуральное и ноль): "))
    if num >= 0:
        print("{}! = {}".format(num, math.factorial(num)))
    else:
        print("Ошибка!")


def ArcCos():
    num = float(input("Число от -1 до 1: "))
    if (num <= 1) and (num >= -1):
        print("arccos({}) = {}".format(num, math.acos(num)))
    else:
        print("Ошибка!")


def Quit():
    quit()


def Calc():
    Information()
    while True:
        oper = str(input("Введите имя операции: "))
        if oper == '+':
            Sum()
        elif oper == '-':
            Subtraction()
        elif oper == '*':
            Multiplication()
        elif oper == '/':
            Division()
        elif oper == 'СТЕПЕНЬ' or oper == 'Степень' or oper == 'степень':
            Power()
        elif oper == 'МОДУЛЬ' or oper == 'Модуль' or oper == 'модуль':
            Abs()
        elif oper == 'РАНДОМ' or oper == 'Рандом' or oper == 'рандом':
            Random()
        elif oper == 'ФАКТОРИАЛ' or oper == 'Факториал' or oper == 'факториал':
            Factorial()
        elif oper == 'АРККОС' or oper == 'Арккос' or oper == 'арккос':
            ArcCos()
        elif oper == 'ВЫЙТИ' or oper == 'Выйти' or oper == 'выйти':
            Quit()
        else:
            print("Нет такой операции!")


Calc()
