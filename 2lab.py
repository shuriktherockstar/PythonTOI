string = str(input("Введите строку: "))

print("Строка без третьего символа: ", end = '')
for it, char in enumerate(string):
    if it == 2: continue
    print(char, end = '')
print()

if string.find('с') != -1:
    print("В строке есть символ \"c\".")
else:
    print("В строке нет символа \"c\".")

print("Длина строки - {}".format(len(string)))
print("Строка без последнего символа - {}".format(string[:-1:]))