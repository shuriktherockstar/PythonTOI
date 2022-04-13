import math
import random


class Calculator:

    @staticmethod
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

    @staticmethod
    def Sum():
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} + {} = {}".format(num1, num2, num1 + num2))

    @staticmethod
    def Subtraction():
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} - {} = {}".format(num1, num2, num1 - num2))

    @staticmethod
    def Multiplication():
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} * {} = {}".format(num1, num2, num1 * num2))

    @staticmethod
    def Division():
        num1 = float(input("Делимое: "))
        num2 = float(input("Делитель: "))
        print("{} * {} = {}".format(num1, num2, num1 / num2))

    @staticmethod
    def Power():
        num1 = float(input("Основание: "))
        num2 = float(input("Степень: "))
        print("{} ^ {} = {}".format(num1, num2, num1 ** num2))

    @staticmethod
    def Abs():
        num = float(input("Число: "))
        print("|{}| = {}".format(num, abs(num)))

    @staticmethod
    def Random():
        print("Случайное число - {}".format(random.random()))

    @staticmethod
    def Factorial():
        num = int(input("Число (только натуральное и ноль): "))
        if num >= 0:
            print("{}! = {}".format(num, math.factorial(num)))
        else:
            print("Ошибка!")

    @staticmethod
    def ArcCos():
        num = float(input("Число от -1 до 1: "))
        if (num <= 1) and (num >= -1):
            print("arccos({}) = {}".format(num, math.acos(num)))
        else:
            print("Ошибка!")

    @staticmethod
    def Calc():
        Calculator.Information()
        while True:
            operation = str(input("Введите имя операции: "))
            if operation == '+':
                Calculator.Sum()
            elif operation == '-':
                Calculator.Subtraction()
            elif operation == '*':
                Calculator.Multiplication()
            elif operation == '/':
                Calculator.Division()
            elif operation == 'СТЕПЕНЬ' or operation == 'Степень' or operation == 'степень':
                Calculator.Power()
            elif operation == 'МОДУЛЬ' or operation == 'Модуль' or operation == 'модуль':
                Calculator.Abs()
            elif operation == 'РАНДОМ' or operation == 'Рандом' or operation == 'рандом':
                Calculator.Random()
            elif operation == 'ФАКТОРИАЛ' or operation == 'Факториал' or operation == 'факториал':
                Calculator.Factorial()
            elif operation == 'АРККОС' or operation == 'Арккос' or operation == 'арккос':
                Calculator.ArcCos()
            elif operation == 'ВЫЙТИ' or operation == 'Выйти' or operation == 'выйти':
                break
            else:
                print("Нет такой операции!")

