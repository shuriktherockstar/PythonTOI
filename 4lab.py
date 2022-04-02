Names = []
Counts = []

for i in range(3):
    word = str(input("Введите название предмета: "))
    Names.append(word)
print()

print("Названия нижним регистром:")
for thing in Names:
    print(thing.lower())
print()

print("Названия верхним регистром:")
for thing in Names:
    print(thing.upper())
print()

print("Первая буква большая, остальные нижним регистром:")
for thing in Names:
    print(thing.capitalize())
print()

for thing in Names:
    number = int(input("Количество предметов - {}".format(thing)))
    Counts.append(number)
print()

for i in range(3):
    Name = Names[i]
    Count = Counts[i]
    print("Количество предметов {} - {}".format(Name, Count).capitalize())
print()