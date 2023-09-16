# Программа, которая принимает целое число от пользователя и
# проверяет, является ли оно положительным, отрицательным или нулем.
num: int = int(input('Введите целое число: '))

# код является примером вложенного тернарного оператора (плохо читается)
result: int = 1 if num > 0 else -1 if num < 0 else 0
print(result)

# оператор if, elif, else
# if num > 0:
#     print(1)
# elif num < 0:
#     print(-1)
# else:
#     print(0)

# оператор match, case
# match num:
#     case x if x > 0:
#         print(1)
#     case x if x < 0:
#         print(-1)
#     case _:
#         print(0)
