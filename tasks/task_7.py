# Программе подается три значения: целое число, дробное число и строка.
# Если хотя бы одно значение истинно, выведите "Да".
# В противном случае выведите "Нет"
num: int = int(input('Введите целое число: '))
fractional_number: float = float(input('Введите дробное число: '))
line: str = input('Введите строку: ')

if num:
    print('Да')
elif fractional_number:
    print('Да')
elif line:
    print('Да')
else:
    print('Нет')
