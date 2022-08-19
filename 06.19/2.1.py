address = input('Введите электронный адрес: ')

if address.count('@') == 1 and address[0] != '@':
    if address.count('.') > 0 and address.find('.') > address.find('@'):
        print('Верно!')
    else:
        print('Неверно!')
else:
    print('Неверно!')

