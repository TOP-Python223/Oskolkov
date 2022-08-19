line = input('Введите текст сообщения: ')
n = len(line) - line.count(' ')
print(f'{(n * 80) // 100} руб. {(n * 80) % 100} коп.')