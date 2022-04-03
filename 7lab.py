def wListCreating():
    print("Введите список слов через запятую: ")
    wList = input().split(", ")
    return(wList)


def wLotsCreating(wList):
    wLots = set(wList)
    LotsLength = len(wLots)
    print("Создано множество из {} слов(-а): ".format(LotsLength))
    print(wLots)
    return wLots, LotsLength


def valListCreating(LotsLength):
    valList = []
    for i in range(LotsLength):
        print("Дайте толкование {} слова".format(i + 1))
        val = input()
        valList.append(val)
    return valList


def DictCreating(wLots, valList):
    Dict = dict(zip(wLots, valList))
    print("Словарь: {}".format(Dict))
    return Dict

# В самой программе a - список слов, b - множество, c - список значений (value), d - словарь


a = wListCreating()
b, bLength = wLotsCreating(a)
c = valListCreating(bLength)
d = DictCreating(b, c)
