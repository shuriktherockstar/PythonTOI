firstNum = int(input("Введите произвольное число: "))
secondNum = int(input("Введите пограничное число: "))
if firstNum > secondNum * 3:
    print("Произвольное число больше пограничного более, чем в три раза")
elif firstNum > secondNum:
    print("Произвольное больше, чем пограничное")
elif firstNum < secondNum:
    print("Пограничное число больше, чем произвольное")
