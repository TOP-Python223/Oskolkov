s = []
while True:
    number = int(input('Введите число: '))
    if number % 7 != 0:
        break
    s += [number]

for i in range(len(s)):
    print(s[i], end=' ')
