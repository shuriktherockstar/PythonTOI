string = str(input("Введите строку: "))

print("Строка без третьего символа: ", end='')

for i, value in enumerate(string):  # i - индекс (0, ..), value - значение
    if i == 2:
        print(end='')
    else:
        print(value, end='')

print()

if string.find('с') != -1:  # -1 - substring не найдена
    print("В строке есть символ \"c\".")
else:
    print("В строке нет символа \"c\".")

print("Длина строки - {}".format(len(string)))
print("Строка без последнего символа - {}".format(string[:-1:]))
