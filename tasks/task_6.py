year: int = int(input('Введите год: '))
number_month: int = int(input('Введите номер месяца: '))

months: list = [1, 3, 5, 7, 8, 10, 12]

is_leap_year: bool = year % 4 == 0 and year % 100 == 0 or year % 400 == 0

if number_month in months and is_leap_year == True:
    print('Да')
else:
    print('Нет')
