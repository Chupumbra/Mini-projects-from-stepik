def func():
    t = 'Hawnj pk swhg xabkna ukq nqj.'
    result = []
    for i in range(25):
        res = ''
        for char in t:
            if char.isalpha():
                if char.isupper():
                    start = ord('A')
                    end = ord('Z')
                if char.islower():
                    start = ord('a')
                    end = ord('z')
                st = chr(start + (ord(char) - start - 1) % (end - start + 1))
                res += st
            else:
                res += char
        result.append(res)
    return res

print(func())


print('Программа "Шифр Цезаря. Чтобы выйти, напишите "стоп"')


flag = True
while flag:
    orientation = input('Выберите направление: шифр/дешифр ')
    if orientation == 'стоп':
        flag = False
        print('Программа завершена')
        break
    language = input('Выберете язык: ру/ен ')
    n = int(input('Введите позицию, на которую нужно зашифровать/расшифровать '))
    text = input('Введите текст ')
    st = ''
    res = ''
    for char in text:
        if char.isalpha():
            if language == "ен":
                if char.isupper():
                    start = ord('A')
                    end = ord('Z')
                if char.islower():
                    start = ord('a')
                    end = ord('z')
            elif language == 'ру':
                if char.isupper():
                    start = ord('А')
                    end = ord('Я')
                if char.islower():
                    start = ord('а')
                    end = ord('я')

            if orientation == 'шифр':
                st = chr(start + (ord(char) - start + n) % (end - start + 1))
            elif orientation == 'дешифр':
                st = chr(start + (ord(char) - start - n) % (end - start + 1))
            else:
                print('Неправильное направление')
                break

            res += st

        else:
            res += char

    print(res)