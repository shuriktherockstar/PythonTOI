firstNum = int(input("Введите произвольное число: "))
secNum = int(input("Введите пограничное число: "))
if firstNum > secNum * 3:
    print("Произвольное число больше пограничного более, чем в три раза")
elif firstNum > secNum:
    print("Произвольное больше, чем пограничное")
elif firstNum < secNum:
    print("Пограничное число больше, чем произвольное")
