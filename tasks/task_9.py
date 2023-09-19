# Программа подается три значения: целое число, дробное число и строка.
# Если хотя бы одно значение истинно, выведите "Да".
# В противном случае выведите "Нет"
whole_number: int = int(input('Введите целое число: '))
fractional_number: float = float(input('Введите дробное число: '))
line: str = input('Введите строку: ')

if any([whole_number, fractional_number, line]):
    print('Да')
else:
    print('Нет')
