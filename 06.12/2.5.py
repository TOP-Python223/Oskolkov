print('!!!Горизонтальные клетки писать латинскими буквами в нижнем регистре, а в вертикальных клетках-цифры от 1 до 8!!!')
a1 = input('Первая горизонтальная клетка: ')
a2 = int(input('Первая вертикальная клетка: '))
b1 = input('Вторая горизонтальная клетка: ')
b2 = int(input('Вторая вертикальная клетка: '))
if (a1 == 'a' or a1 == 'c' or a1 == 'e' or a1 == 'g') and (a2 % 2 != 0):
    if (b1 == 'a' or b1 == 'c' or b1 == 'e' or b1 == 'g') and (b2 % 2 != 0):
        print('Да')
    elif (b1 == 'b' or b1 == 'd' or b1 == 'f' or b1 == 'h') and (b2 % 2 == 0):
        print('Да')
    else:
        print('Нет')
elif (a1 == 'b' or a1 == 'd' or a1 == 'f' or a1 == 'h') and (a2 % 2 == 0):
    if (b1 == 'a' or b1 == 'c' or b1 == 'e' or b1 == 'g') and (b2 % 2 != 0):
        print('Да')
    elif (b1 == 'b' or b1 == 'd' or b1 == 'f' or b1 == 'h') and (b2 % 2 == 0):
        print('Да')
    else:
        print('Нет')
elif (a1 == 'a' or a1 == 'c' or a1 == 'e' or a1 == 'g') and (a2 % 2 == 0):
    if (b1 == 'a' or b1 == 'c' or b1 == 'e' or b1 == 'g') and (b2 % 2 == 0):
        print('Да')
    elif (b1 == 'b' or b1 == 'd' or b1 == 'f' or b1 == 'h') and (b2 % 2 != 0):
        print('Да')
    else:
        print('Нет')
elif (a1 == 'b' or a1 == 'd' or a1 == 'f' or a1 == 'h') and (a2 % 2 != 0):
    if (b1 == 'a' or b1 == 'c' or b1 == 'e' or b1 == 'g') and (b2 % 2 == 0):
        print('Да')
    elif (b1 == 'b' or b1 == 'd' or b1 == 'f' or b1 == 'h') and (b2 % 2 != 0):
        print('Да')
    else:
        print('Нет')
else:
    print('Неверные данные!')

