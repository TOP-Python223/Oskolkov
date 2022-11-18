print('!!!Горизонтальные клетки писать латинскими буквами в нижнем регистре, а в вертикальных клетках-цифры от 1 до 8!!!')
a1 = input('Первая горизонтальная клетка: ')
a2 = int(input('Первая вертикальная клетка: '))
b1 = input('Вторая горизонтальная клетка: ')
b2 = int(input('Вторая вертикальная клетка: '))
if 0 < a2 < 9 and 0 < b2 < 9:
    if a1 == 'a':
        if (a1 <= 'b') and (a2 - 1 <= b2 <= a2 + 1):
            print('Да')
        else:
            print('Нет')
    elif a1 == 'b':
        if ('a' <= b1 <= 'c') and (a2 - 1 <= b2 <= a2 + 1):
            print('Да')
        else:
            print('Нет')
    elif a1 == 'c':
        if ('b' <= b1 <= 'd') and (a2 - 1 <= b2 <= a2 + 1):
            print('Да')
        else:
            print('Нет')
    elif a1 == 'd':
        if ('c' <= b1 <= 'e') and (a2 - 1 <= b2 <= a2 + 1):
            print('Да')
        else:
            print('Нет')
    elif a1 == 'e':
        if ('d' <= b1 <= 'f') and (a2 - 1 <= b2 <= a2 + 1):
            print('Да')
        else:
            print('Нет')
    elif a1 == 'f':
        if ('e' <= b1 <= 'g') and (a2 - 1 <= b2 <= a2 + 1):
            print('Да')
        else:
            print('Нет')
    elif a1 == 'g':
        if ('f' <= b1 <= 'h') and (a2 - 1 <= b2 <= a2 + 1):
            print('Да')
        else:
            print('Нет')
    elif a1 == 'h':
        if ('g' <= b1 <= 'h') and (a2 - 1 <= b2 <= a2 + 1):
            print('Да')
        else:
            print('Нет')
    else:
        print('Неверные данные!')
else:
    print('Неправильно введены данные в вертикальных клетках!')
