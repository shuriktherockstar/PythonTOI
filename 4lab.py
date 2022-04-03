veggies = []
counter = []

for i in range(3):
    print("Введите название {} овоща - ".format(i+1), end='')
    veg = str(input())
    veggies.append(veg)
print()

print("Названия нижним регистром:")
for veggie in veggies:
    print("[{}]".format(veggie.lower()), end=' ')
print()

print("Названия верхним регистром:")
for veggie in veggies:
    print("[{}]".format(veggie.upper()), end=' ')
print()

print("Первая буква верхним регистром, остальные - нижним:")
for veggie in veggies:
    print("[{}]".format(veggie.capitalize()), end=' ')
print()

for veggie in veggies:
    print("Количество овощей \"{}\" - ".format(veggie), end='')
    count = input()
    counter.append(count)
print()

for i in range(3):
    veggie = veggies[i]
    count = counter[i]
    print("Количество овощей \"{}\" - {}".format(veggie.capitalize(), count))
print()

