number1 = int(input('Введите натуральное число: '))
s = 0
for i in range(number1):
    number2 = int(input())
    if number2 > 0:
        s += number2
print(s)