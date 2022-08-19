number = int(input('Введите число: '))
x1 = number[0] + number[1] + number[2]
x2 = number[3] + number[4] + number[5]
if x1 == x2:
    print('Счастливый билет')
else:
    print('Несчастливый билет')