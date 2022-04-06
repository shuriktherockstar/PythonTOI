def wListCreating():
    print("Введите список слов через запятую: ")
    w_list = input().split(", ")
    return w_list


def wLotsCreating(w_list):
    w_lots = set(w_list)
    lots_length = len(w_lots)
    print("Создано множество из {} слов(-а): ".format(lots_length))
    print(w_lots)
    return w_lots, lots_length


def valListCreating(lots_length):
    val_list = []
    for i in range(lots_length):
        print("Дайте толкование {} слова".format(i + 1))
        val = input()
        val_list.append(val)
    return val_list


def DictCreating(w_lots, val_list):
    dictionary = dict(zip(w_lots, val_list))
    print("Словарь: {}".format(dictionary))
    return dictionary

# В самой программе a - список слов, b - множество, c - список значений (value), d - словарь


a = wListCreating()
b, bLength = wLotsCreating(a)
c = valListCreating(bLength)
d = DictCreating(b, c)
