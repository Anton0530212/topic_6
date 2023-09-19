# Программа должна определить, является ли введенная буква гласной или согласной
ALPHABETS = {
    "en_vowels": "AEIOU",
    "en_consonants": "BCDFGHJKLMNPQRSTVWXYZ",
    "ru_vowels": "АЕЁИОУЫЭЮЯ",
    "ru_consonants": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ",
}

print("Добро пожаловать в программу \"Буква-Детектив\"!", end="\n\n")
print('Выберите алфавит:', '1.Латинский', '2.Кириллица', sep='\n', end="\n\n")

alphabet: int = int(input('Введите номер алфавита: '))

if alphabet == 1:
    letter: str = input('Введите букву латинского алфавита: ')
    if letter in ALPHABETS["en_vowels"]:
        print(letter, '- гласная буква')
    elif letter in ALPHABETS["en_consonants"]:
        print(letter, '- согласная буква')
    else:
        print('Упс! Неизвестная буква. Попробуйте другую!')
elif alphabet == 2:
    letter: str = input('Введите букву кириллицы: ')
    if letter in ALPHABETS["ru_vowels"]:
        print(letter, '- гласная буква')
    elif letter in ALPHABETS["ru_consonants"]:
        print(letter, '- согласная буква')
    else:
        print('Упс! Неизвестная буква. Попробуйте другую!')
else:
    print('Упс! Выбран неверный режим. Попробуйте ещё раз...')
