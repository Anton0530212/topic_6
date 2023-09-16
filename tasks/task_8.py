# Программа, которая трансформирует полученные значения по условию задачи
num_1: int = int(input('Введите первое число: '))
num_2: int = int(input('Введите второе число: '))
line: str = input('Введите магическую операцию: ')

if line == "Призыв":
    print(float(num_1 + num_2))
elif line == "Трансформация":
    print(float(abs(num_1) + abs(num_2)))
elif line == "Объединение":
    print(float(num_1 * num_2))
elif line == "Исчезновение":
    num_1 = 0
    print(num_1, num_2)
elif num_2 == 0:
    print('Ошибка: Второе число равно нулю!')
else:
    print('Ошибка: Некорректная операция')
