line = []
number = int(input('Введите число: '))
for i in range (number):
    line += [chr(ord('а') + i)]
print(line)