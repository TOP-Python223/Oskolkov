a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))
if a > 0 and b > 0 and c > 0:
    print(a + b + c)
elif a > 0 and b > 0 and c < 0:
    print(a + b)
elif a > 0 and c > 0 and b < 0:
    print(a + c)
elif b > 0 and c > 0 and a < 0:
    print(b + c)
elif a > 0 and b < 0 and c < 0:
    print(a)
elif a < 0 and b > 0 and c < 0:
    print(b)
elif a < 0 and b < 0 and c > 0:
    print(c)
else:
    print('Нет положительных чисел!')
