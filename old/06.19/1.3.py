number1 = int(input('Введите число: '))
s = 0
for i in range (1, number1 + 1):
    number2 = number1 % i
    if number2 == 0:
        s += i
print(s)