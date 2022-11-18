age = int(input('Введите ваш возраст: '))
if 0 <= age <= 13:
    print('детство')
elif 14 <= age <= 24:
    print('молодость')
elif 25 <= age <= 59:
    print('зрелость')
elif 60 <= age <= 150:
    print('старость')
else:
    print('неверные данные')