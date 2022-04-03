print("Введите список слов через запятую: ")
wList = input().split(", ")  # ввод строки
wLots = set(wList)  # формирование множества
LotsLength = len(wLots)
print("Создано множество из {} слов(-а): ".format(LotsLength))
print(wLots)

valList = []
for i in range(LotsLength):
    print("Дайте толкование {} слова".format(i + 1))
    val = input()
    valList.append(val)

Dict = dict(zip(wLots, valList))
print("Словарь: {}".format(Dict))
