# не сделано
year: int = int(input('Введите год: '))
month: int = int(input('Введите номер месяца: '))

# leap_year =
if year % 4 == 0 and year % 400 == 0:
    print('Да')
elif year % 100 == 0:
    print('Нет')
#  не понимаю условие